from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory data structure to simulate storage
fake_db = []
unique_id_counter = 1  # Initialize a counter for assigning unique IDs

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/store-data")
async def store_data():
    return {"message": "store_data"}

@app.post("/store-data/{item}")
async def store_data(item: str):
    global unique_id_counter
    
    # Assign a unique ID to each piece of data
    data = {"id": unique_id_counter, "item": item}
    
    # Increment the unique ID counter
    unique_id_counter += 1
    
    # Simulate storing data in the "database"
    fake_db.append(data)
    
    # Return a successful response
    return {"message": "Data stored successfully", "data": data}


@app.delete("/store-data/{item_id}")
async def delete_data(item_id: int):
    # Check if the item with the specified ID exists in the "database"
    for data in fake_db:
        if data["id"] == item_id:
            # Remove the item
            fake_db.remove(data)
            return {"message": f"Data deleted successfully for item with ID: {item_id}"}
    
    # Return 404 Not Found if the item doesn't exist
    raise HTTPException(status_code=404, detail=f"Item with ID '{item_id}' not found")


@app.get("/store-data/{item_id}")
async def retrieve_data(item_id: int):
    # Check if the item with the specified ID exists in the "database"
    for data in fake_db:
        if data["id"] == item_id:
            # Return the item
            return {"message": f"Data retrieved successfully for item with ID: {item_id}", "data": data}
    
    # Return 404 Not Found if the item doesn't exist
    raise HTTPException(status_code=404, detail=f"Item with ID '{item_id}' not found")

@app.put("/store-data/{item_id}")
async def update_data(item_id: int, updated_item: str):
    # Check if the item with the specified ID exists in the "database"
    for data in fake_db:
        if data["id"] == item_id:
            # Update the item
            data["item"] = updated_item
            return {"message": f"Data updated successfully for item with ID: {item_id}", "data": data}

@app.post("/welcome")
async def welcome(payload: dict):
    global unique_id_counter
    
    # Check if the payload contains a "name" key
    if "name" not in payload:
        raise HTTPException(status_code=422, detail="Name not provided in the payload")

    # Assign a unique ID to each welcome message
    welcome_data = {"id": unique_id_counter, "name": payload["name"]}
    
    # Increment the unique ID counter
    unique_id_counter += 1
    
    # Save structured data, including the name
    fake_db.append(welcome_data)
    
    # Return a welcome message with the name
    return {"message": f"Welcome, {payload['name']}!", "data": welcome_data}
