# RATLS-Assignment-AmoghK

## Flask API with Authentication and Database Operations

This project provides a simple Flask API with authentication and database operations. It includes functionality to retrieve, store, edit, and delete data with each piece of data having a unique identity.

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [Flask-JWT](https://pythonhosted.org/Flask-JWT/)
- [Flask-SQLAlchemy](https://pypi.org/project/Flask-SQLAlchemy/)

## Getting Started

1. **Download the Script:**
   - Download the provided script folder and save it to your computer.

2. **Install Dependencies:**
   - Open a terminal or command prompt.
   - Navigate to the directory where you saved the script.
   - Run the following command to install the required Python packages:
     ```bash
     pip install Flask Flask-RESTful Flask-JWT Flask-SQLAlchemy
     ```

3. **Run the Script:**
   - Run the Flask development server:
     ```bash
     python app.py
     ```
   - The API will be accessible at `http://127.0.0.1:5000/`.

4. **Testing the API:**
   - Use tools like `curl`, [Postman](https://www.postman.com/), or any other API testing tool.
   - Obtain a JWT token by sending a POST request to `http://127.0.0.1:5000/auth` with a JSON payload containing a valid username and password.
   - Use the obtained token in the Authorization header for subsequent requests to the API endpoints.

5. **Clean Up:**
   - Stop the Flask development server by pressing `Ctrl + C` in the terminal.

## API Endpoints

- **Retrieve Data (GET):** `http://127.0.0.1:5000/item/<int:id>`
- **Store Data (POST):** `http://127.0.0.1:5000/item/<int:id>` (with JSON payload)
- **Edit and Replace (PUT):** `http://127.0.0.1:5000/item/<int:id>` (with JSON payload)
- **Delete Data (DELETE):** `http://127.0.0.1:5000/item/<int:id>`

## Database

- The script uses SQLite as the database and creates a file named `mydatabase.db`.

## Note

- This is a simple demonstration, and in a production environment, you would likely use a more robust database system (e.g., PostgreSQL, MySQL) and implement proper security measures.
