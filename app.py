from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required
from flask_sqlalchemy import SQLAlchemy
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'write_your_secret_key_here'
api = Api(app)
db = SQLAlchemy(app)

jwt = JWT(app, authenticate, identity) 


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

# Create tables before the first request is handled
@app.before_first_request
def create_tables():
    db.create_all()

# Resource to interact with the API and database
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('data', type=str, required=True, help='This field cannot be left blank')

    @jwt_required()
    def get(self, _id):
        # Retrieve data from the database using the unique identifier (id)
        item = UserModel.find_by_id(_id)
        if item:
            return {'item': {'id': item.id, 'username': item.username, 'password': item.password}}
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def post(self, _id):
        # Store data in the database with a unique identifier (id) and user's name
        data = Item.parser.parse_args()
        if UserModel.find_by_id(_id):
            return {'message': f'Item with id {_id} already exists.'}, 400

        user = UserModel(id=_id, username=f'User {_id}', password=data['data'])
        user.save_to_db()
        return {'message': f'Welcome, {user.username}! Item created successfully.'}, 201

    @jwt_required()
    def put(self, _id):
        # Edit and replace existing data in the database using the unique identifier (id)
        data = Item.parser.parse_args()
        item = UserModel.find_by_id(_id)

        if item:
            item.password = data['data']
            item.save_to_db()
            return {'message': 'Item updated successfully.'}
        else:
            return {'message': 'Item not found'}, 404

    @jwt_required()
    def delete(self, _id):
        # Delete data from the database using the unique identifier (id)
        item = UserModel.find_by_id(_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return {'message': 'Item deleted successfully.'}
        else:
            return {'message': 'Item not found'}, 404

# Endpoint for interacting with the API
api.add_resource(Item, '/item/<int:_id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
