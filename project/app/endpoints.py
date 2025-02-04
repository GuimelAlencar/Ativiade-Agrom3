from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=schemas.ItemRead)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/users/{user_id}", response_model=schemas.ItemRead)
def get_item(user_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == user_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/users/{user_id}", response_model=schemas.ItemRead)
def delete_item(user_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == user_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return item
