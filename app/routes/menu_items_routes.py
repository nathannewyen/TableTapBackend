from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.menu_item import MenuItemCreate
from app.repositories.menu_item_repository import create_menu_item
from app.db.database import get_db

router = APIRouter()

@router.post("/admin/menu-items", status_code=status.HTTP_201_CREATED)
def add_menu_item(menu_item: MenuItemCreate, db: Session = Depends(get_db)):
    new_item = create_menu_item(db, menu_item)
    return new_item