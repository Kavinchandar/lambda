from fastapi import FastAPI
from models import Item
from services import create_item_service, get_item_service, list_items_service

app = FastAPI()


#root
@app.get("/")
def root():
    return {"message": "Hello, World!"}


#post requests
@app.post('/items', response_model=list[Item])
def create_item(item: Item):
    return create_item_service(item)


#get requests
@app.get('/items/{item_id}', response_model=Item)
def read_item(item_id: int) -> Item:
    return get_item_service(item_id)

@app.get('/items')
def list_items(limit: int = 10):
    return list_items_service(limit)