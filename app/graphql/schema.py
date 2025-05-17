import strawberry
from app.graphql.mutations.category_mutations import CategoryMutation
from app.graphql.mutations.menu_item_mutations import MenuItemMutation
from app.graphql.mutations.restaurant_mutations import RestaurantMutation
from app.graphql.types.category import CategoryType
from app.graphql.types.menu_item import MenuItemType
from typing import List
from app.db.database import get_db, SessionLocal
from app.models.menu import Category
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import Session

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    def categories(self) -> List[CategoryType]:
        """Get all categories with their menu items"""
        db = SessionLocal()
        try:
            categories = db.query(Category).options(joinedload(Category.menu_items)).all()
            return [
                CategoryType(
                    id=category.id,
                    name=category.name,
                    description=category.description,
                    imgUrl=category.img_url,
                    menuItems=[
                        MenuItemType(
                            id=item.id,
                            name=item.name,
                            description=item.description,
                            price=item.price,
                            imageUrl=item.img_url,
                            isAvailable=item.available
                        ) for item in category.menu_items
                    ]
                ) for category in categories
            ]
        finally:
            db.close()

@strawberry.type
class Mutation(CategoryMutation, MenuItemMutation, RestaurantMutation):
    pass

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
) 