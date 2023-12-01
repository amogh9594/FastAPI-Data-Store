# RATLS-Assignment-AmoghK

# FastAPI Store Data App
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
