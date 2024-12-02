from fastapi import FastAPI, Request
from motor.motor_asyncio import AsyncIOMotorClient
from rich.pretty import pprint
import asyncio
from pymongo.errors import PyMongoError
from typing import Optional
import uvicorn

app = FastAPI()

# Initialize MongoDB async client globally (this avoids creating a new connection on every request)
client = AsyncIOMotorClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
db = client['codewise']  # Replace with your database name
collection = db['telemetery']  # Replace with your collection name

# In-memory store to hold data temporarily before inserting
data_buffer = []

# Function to insert aggregated data every 5 seconds
async def insert_data_periodically():
    while True:
        if data_buffer:
            # Aggregation logic: Example is counting how many entries were added
            # aggregate_data = {
            #     "total_entries": len(data_buffer),
            #     "data": data_buffer
            # }
            try:
                # Insert aggregated data into MongoDB
                await collection.insert_many(data_buffer)
                pprint({"status": "success", "message": "Data aggregated and inserted successfully."})
            except PyMongoError as e:
                pprint({"status": "error", "message": f"MongoDB error: {str(e)}"})
            except Exception as e:
                pprint({"status": "error", "message": f"Error: {str(e)}"})
            # Clear the buffer after insertion
            data_buffer.clear()

        # Wait for 5 seconds before the next insert
        await asyncio.sleep(5)

# Start the periodic task
@app.on_event("startup")
async def start_periodic_task():
    asyncio.create_task(insert_data_periodically())

# @app.post("/batch")
# async def batch(path: str, request: Request):
#     """
#     This is a catch-all route for handling dynamic paths and different HTTP methods.
#     Data will be temporarily stored in an in-memory buffer and inserted periodically.
#     """

#     try:
#         payload = await request.json()
#         batch = payload.get("batch", [])
#     except Exception as e:
#         payload = None

#     # Handle POST request on the "batch" path to temporarily store data
#     if payload is not None and len(batch) > 0:
#         data_buffer.append(batch)
#         pprint({"status": "success", "message": "Data received and added to buffer."})

#     # Log received data for debugging purposes
#     pprint(payload, expand_all=True)

#     # return {"path": path, "method": request.method, "payload": payload}

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def catch_all(path: str, request: Request):
    """
    This is a catch-all route for handling dynamic paths and different HTTP methods.
    Data will be temporarily stored in an in-memory buffer and inserted periodically.
    """

    # Initialize payload as None by default
    payload: Optional[dict] = None

    try:
        payload = await request.json()
        batch = payload.get("batch", []) if payload is not None else []
        if len(batch) > 0:
            data_buffer.append(batch)
    except Exception as e:
        payload = None

    pprint(payload, expand_all=True)


if __name__ == "__main__":
    uvicorn.run(app)
