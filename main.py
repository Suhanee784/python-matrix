from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple API")


# Request model
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


# Sample endpoint: Root
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}


# Sample endpoint: Read item with path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}


# Sample endpoint: Create item with request body
@app.post("/items/")
def create_item(item: Item):
    return {"status": "Item created", "item": item}



    