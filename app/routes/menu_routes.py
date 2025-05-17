from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.database import get_db
from app.schemas.menu import (
    Category, CategoryCreate, CategoryUpdate,
    MenuItem, MenuItemCreate, MenuItemUpdate, MenuItemDetail
)
from app.services.menu_service import MenuService

router = APIRouter(
    prefix="/api/menu",
    tags=["menu"],
    responses={404: {"description": "Not found"}},
)

# Category routes
@router.post("/categories/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    result = MenuService.create_category(db, category)
    if not result["success"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result["message"])
    return result["data"]

@router.get("/categories/", response_model=List[Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    result = MenuService.get_all_categories(db, skip, limit)
    return result["data"]

@router.get("/categories/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    result = MenuService.get_category(db, category_id)
    if not result["success"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result["message"])
    return result["data"]

@router.put("/categories/{category_id}", response_model=Category)
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    result = MenuService.update_category(db, category_id, category)
    if not result["success"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result["message"])
    return result["data"]

@router.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    result = MenuService.delete_category(db, category_id)
    if not result["success"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result["message"])
    return None

# Menu Item routes
@router.post("/items/", response_model=MenuItem, status_code=status.HTTP_201_CREATED)
def create_menu_item(menu_item: MenuItemCreate, db: Session = Depends(get_db)):
    result = MenuService.create_menu_item(db, menu_item)
    if not result["success"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result["message"])
    return result["data"]

@router.get("/items/", response_model=List[MenuItem])
def read_menu_items(
    category_id: Optional[int] = None,
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    if category_id:
        result = MenuService.get_menu_items_by_category(db, category_id, skip, limit)
        if not result["success"]:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result["message"])
    else:
        result = MenuService.get_all_menu_items(db, skip, limit)
    return result["data"]

@router.get("/items/{menu_item_id}", response_model=MenuItemDetail)
def read_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    result = MenuService.get_menu_item(db, menu_item_id)
    if not result["success"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result["message"])
    return result["data"]

@router.put("/items/{menu_item_id}", response_model=MenuItem)
def update_menu_item(menu_item_id: int, menu_item: MenuItemUpdate, db: Session = Depends(get_db)):
    result = MenuService.update_menu_item(db, menu_item_id, menu_item)
    if not result["success"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result["message"])
    return result["data"]

@router.delete("/items/{menu_item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    result = MenuService.delete_menu_item(db, menu_item_id)
    if not result["success"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result["message"])
    return None
