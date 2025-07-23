from models import Item
from fastapi import HTTPException

items = []

def create_item_service(item: Item):
    items.append(item)
    return items

def get_item_service(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    return items[item_id]

def list_items_service(limit):
    if limit < 1:
        raise HTTPException(status_code=404, detail=f"Limit must be at least 1, given {limit}")
    return items[:limit]