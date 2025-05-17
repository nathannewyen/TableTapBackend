from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from app.models.menu import Category, MenuItem, MenuItemCustomization

class MenuRepository:
    # Category CRUD operations
    @staticmethod
    def create_category(db: Session, name: str, description: Optional[str] = None) -> Category:
        category = Category(name=name, description=description)
        db.add(category)
        db.commit()
        db.refresh(category)
        return category
    
    @staticmethod
    def get_category(db: Session, category_id: int) -> Optional[Category]:
        return db.query(Category).filter(Category.id == category_id).first()
    
    @staticmethod
    def get_category_by_name(db: Session, name: str) -> Optional[Category]:
        return db.query(Category).filter(Category.name == name).first()
    
    @staticmethod
    def get_all_categories(db: Session, skip: int = 0, limit: int = 100) -> List[Category]:
        return db.query(Category).offset(skip).limit(limit).all()
    
    @staticmethod
    def update_category(db: Session, category_id: int, name: Optional[str] = None, 
                         description: Optional[str] = None) -> Optional[Category]:
        category = db.query(Category).filter(Category.id == category_id).first()
        if category:
            if name is not None:
                category.name = name
            if description is not None:
                category.description = description
            db.commit()
            db.refresh(category)
        return category
    
    @staticmethod
    def delete_category(db: Session, category_id: int) -> bool:
        category = db.query(Category).filter(Category.id == category_id).first()
        if category:
            db.delete(category)
            db.commit()
            return True
        return False
    
    # MenuItem CRUD operations
    @staticmethod
    def create_menu_item(db: Session, menu_item_data: dict) -> MenuItem:
        menu_item = MenuItem(**menu_item_data)
        db.add(menu_item)
        db.commit()
        db.refresh(menu_item)
        return menu_item
    
    @staticmethod
    def get_menu_item(db: Session, menu_item_id: int) -> Optional[MenuItem]:
        return db.query(MenuItem).filter(MenuItem.id == menu_item_id).first()
    
    @staticmethod
    def get_menu_item_detail(db: Session, menu_item_id: int) -> Optional[MenuItem]:
        return db.query(MenuItem).options(
            joinedload(MenuItem.category),
            joinedload(MenuItem.customizations)
        ).filter(MenuItem.id == menu_item_id).first()
    
    @staticmethod
    def get_all_menu_items(db: Session, skip: int = 0, limit: int = 100) -> List[MenuItem]:
        return db.query(MenuItem).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_menu_items_by_category(db: Session, category_id: int, 
                                   skip: int = 0, limit: int = 100) -> List[MenuItem]:
        return db.query(MenuItem).filter(
            MenuItem.category_id == category_id
        ).offset(skip).limit(limit).all()
    
    @staticmethod
    def update_menu_item(db: Session, menu_item_id: int, update_data: dict) -> Optional[MenuItem]:
        menu_item = db.query(MenuItem).filter(MenuItem.id == menu_item_id).first()
        if menu_item:
            for key, value in update_data.items():
                if value is not None:
                    setattr(menu_item, key, value)
            db.commit()
            db.refresh(menu_item)
        return menu_item
    
    @staticmethod
    def delete_menu_item(db: Session, menu_item_id: int) -> bool:
        menu_item = db.query(MenuItem).filter(MenuItem.id == menu_item_id).first()
        if menu_item:
            db.delete(menu_item)
            db.commit()
            return True
        return False
    
    # MenuItemCustomization CRUD operations
    @staticmethod
    def create_customization(db: Session, customization_data: dict) -> MenuItemCustomization:
        customization = MenuItemCustomization(**customization_data)
        db.add(customization)
        db.commit()
        db.refresh(customization)
        return customization
    
    @staticmethod
    def get_menu_item_customizations(db: Session, menu_item_id: int) -> List[MenuItemCustomization]:
        return db.query(MenuItemCustomization).filter(
            MenuItemCustomization.menu_item_id == menu_item_id
        ).all()
