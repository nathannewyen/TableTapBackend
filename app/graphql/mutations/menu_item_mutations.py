import strawberry
from sqlalchemy.orm import Session
from app.models.menu_item import MenuItem
from app.graphql.types.menu_item import MenuItemType, MenuItemInput
from app.db.database import get_db

@strawberry.type
class MenuItemMutation:
    @strawberry.mutation
    async def create_menu_item(
        self,
        input: MenuItemInput
    ) -> MenuItemType:
        db = next(get_db())
        
        # Create new menu item
        db_menu_item = MenuItem(
            name=input.name,
            description=input.description,
            price=input.price,
            img_url=input.imageUrl,
            available=input.isAvailable,
            category=input.categoryId
        )
        
        try:
            db.add(db_menu_item)
            db.commit()
            db.refresh(db_menu_item)
            
            return MenuItemType(
                id=db_menu_item.id,
                name=db_menu_item.name,
                description=db_menu_item.description,
                price=db_menu_item.price,
                imageUrl=db_menu_item.img_url,
                isAvailable=db_menu_item.available
            )
        except Exception as e:
            db.rollback()
            raise Exception(f"Failed to create menu item: {str(e)}") 