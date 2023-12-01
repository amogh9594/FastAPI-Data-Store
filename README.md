# RATLS-Assignment-AmoghK

## FastAPI Store Data App
A FastAPI app for storing, updating, deleting, and retrieving data.

## Endpoints

- `/store-data/{item}`: Stores the given item.
- `/store-data/{item_id}`: Retrieves the item with the specified ID.
- `/store-data/{item_id}`: Deletes the item with the specified ID.
- `/store-data/{item_id}`: Updates the item with the specified ID.
- `/welcome`: Sends a welcome message to the given name.

## Setup

- Ensure Python is installed on your system.
- Install FastAPI using the following command: `pip install fastapi`.
- Install an ASGI server like Uvicorn using the following command: `pip install uvicorn`.
- Start the FastAPI server by running the following command: `uvicorn main:app --reload`.

## Usage

1. Start the server using the command mentioned in the Setup section.
2. Use a REST client like Postman or curl to interact with the server.

Here are some examples of how to use the REST client:

### Example

Welcome message : `Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/welcome" -Body '{"name": "Amogh"}' -ContentType "application/json"`

Delete : `Invoke-RestMethod -Method Delete -Uri "http://127.0.0.1:8000/store-data/Amogh"`

Post : `Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/store-data/Amogh"`

Get : `Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:8000/store-data/AmoghK"`

Put : `Invoke-RestMethod -Method Put -Uri "http://127.0.0.1:8000/store-data/1?updated_item=John%20Doe" -ContentType "application/json"`

