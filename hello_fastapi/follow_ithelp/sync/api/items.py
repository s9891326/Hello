from fastapi import APIRouter
from hello_fastapi.follow_ithelp.sync.database.fake_db import get_db
from hello_fastapi.follow_ithelp.schemas import items as ItemSchema

router = APIRouter(
    tags=["items"],
    prefix="/api"
)
fake_db = get_db()


@router.get("/items/{item_id}")
def get_items_without_typing(item_id, qry):
    if item_id not in fake_db["items"]:
        return {"error": "Item not found"}
    return {"item": fake_db["items"][item_id], "query": qry}


@router.get("/items/{item_id}", response_model=ItemSchema.ItemRead)
def get_item_by_id(item_id: int, qry: str = None):
    if item_id not in fake_db["items"]:
        return {"error": "Item not found"}
    return fake_db["items"][item_id]


@router.post("/items", response_model=ItemSchema.ItemCreate)
def create_items(item: ItemSchema.ItemCreate):
    fake_db["items"][item.id] = item
    return item


@router.delete("/items/{item_id}")
def delete_items(item_id: int):
    item = fake_db["items"].pop(item_id)
    return item
