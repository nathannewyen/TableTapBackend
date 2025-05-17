from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any
from app.repositories.menu_repository import MenuRepository
from app.schemas.menu import CategoryCreate, CategoryUpdate, MenuItemCreate, MenuItemUpdate

class MenuService:
    # Category services
    @staticmethod
    def create_category(db: Session, category: CategoryCreate) -> Dict[str, Any]:
        # Check if category with the same name already exists
        existing_category = MenuRepository.get_category_by_name(db, category.name)
        if existing_category:
            return {"success": False, "message": "Category already exists", "data": None}
        
        # Create new category
        new_category = MenuRepository.create_category(
            db=db, name=category.name, description=category.description
        )
        return {"success": True, "message": "Category created successfully", "data": new_category}
    
    @staticmethod
    def get_all_categories(db: Session, skip: int = 0, limit: int = 100) -> Dict[str, Any]:
        categories = MenuRepository.get_all_categories(db, skip, limit)
        return {"success": True, "message": "Categories retrieved successfully", "data": categories}
    
    @staticmethod
    def get_category(db: Session, category_id: int) -> Dict[str, Any]:
        category = MenuRepository.get_category(db, category_id)
        if not category:
            return {"success": False, "message": "Category not found", "data": None}
        return {"success": True, "message": "Category retrieved successfully", "data": category}
    
    @staticmethod
    def update_category(db: Session, category_id: int, category_update: CategoryUpdate) -> Dict[str, Any]:
        updated_category = MenuRepository.update_category(
            db=db,
            category_id=category_id,
            name=category_update.name,
            description=category_update.description
        )
        if not updated_category:
            return {"success": False, "message": "Category not found", "data": None}
        return {"success": True, "message": "Category updated successfully", "data": updated_category}
    
    @staticmethod
    def delete_category(db: Session, category_id: int) -> Dict[str, Any]:
        # Check if category exists
        category = MenuRepository.get_category(db, category_id)
        if not category:
            return {"success": False, "message": "Category not found", "data": None}
        
        # Check if there are menu items in this category
        menu_items = MenuRepository.get_menu_items_by_category(db, category_id)
        if menu_items:
            return {
                "success": False, 
                "message": "Cannot delete category that has menu items. Remove items first.",
                "data": None
            }
        
        # Delete category
        result = MenuRepository.delete_category(db, category_id)
        return {"success": result, "message": "Category deleted successfully", "data": None}
    
    # MenuItem services
    @staticmethod
    def create_menu_item(db: Session, menu_item: MenuItemCreate) -> Dict[str, Any]:
        # Check if category exists
        category = MenuRepository.get_category(db, menu_item.category_id)
        if not category:
            return {"success": False, "message": "Category not found", "data": None}
        
        # Create menu item
        menu_item_data = menu_item.model_dump()
        new_menu_item = MenuRepository.create_menu_item(db=db, menu_item_data=menu_item_data)
        return {"success": True, "message": "Menu item created successfully", "data": new_menu_item}
    
    @staticmethod
    def get_all_menu_items(db: Session, skip: int = 0, limit: int = 100) -> Dict[str, Any]:
        menu_items = MenuRepository.get_all_menu_items(db, skip, limit)
        return {"success": True, "message": "Menu items retrieved successfully", "data": menu_items}
    
    @staticmethod
    def get_menu_items_by_category(db: Session, category_id: int, 
                                   skip: int = 0, limit: int = 100) -> Dict[str, Any]:
        # Check if category exists
        category = MenuRepository.get_category(db, category_id)
        if not category:
            return {"success": False, "message": "Category not found", "data": None}
        
        menu_items = MenuRepository.get_menu_items_by_category(db, category_id, skip, limit)
        return {"success": True, "message": "Menu items retrieved successfully", "data": menu_items}
    
    @staticmethod
    def get_menu_item(db: Session, menu_item_id: int) -> Dict[str, Any]:
        menu_item = MenuRepository.get_menu_item_detail(db, menu_item_id)
        if not menu_item:
            return {"success": False, "message": "Menu item not found", "data": None}
        return {"success": True, "message": "Menu item retrieved successfully", "data": menu_item}
    
    @staticmethod
    def update_menu_item(db: Session, menu_item_id: int, menu_item_update: MenuItemUpdate) -> Dict[str, Any]:
        # Check if menu item exists
        menu_item = MenuRepository.get_menu_item(db, menu_item_id)
        if not menu_item:
            return {"success": False, "message": "Menu item not found", "data": None}
        
        # If category ID is being updated, check if the new category exists
        if menu_item_update.category_id is not None:
            category = MenuRepository.get_category(db, menu_item_update.category_id)
            if not category:
                return {"success": False, "message": "Category not found", "data": None}
        
        # Update menu item
        update_data = {k: v for k, v in menu_item_update.model_dump().items() if v is not None}
        updated_menu_item = MenuRepository.update_menu_item(db, menu_item_id, update_data)
        return {"success": True, "message": "Menu item updated successfully", "data": updated_menu_item}
    
    @staticmethod
    def delete_menu_item(db: Session, menu_item_id: int) -> Dict[str, Any]:
        # Check if menu item exists
        menu_item = MenuRepository.get_menu_item(db, menu_item_id)
        if not menu_item:
            return {"success": False, "message": "Menu item not found", "data": None}
        
        # Delete menu item
        result = MenuRepository.delete_menu_item(db, menu_item_id)
        return {"success": result, "message": "Menu item deleted successfully", "data": None}