import strawberry
from sqlalchemy.orm import Session
from app.models.menu import Category
from app.graphql.types.category import CategoryType, CategoryInput, UpdateCategoryInput
from app.db.database import get_db
from typing import Optional

@strawberry.type
class CategoryMutation:
    @strawberry.mutation
    async def create_category(
        self, 
        input: CategoryInput
    ) -> CategoryType:
        db = next(get_db())
        
        # Create new category
        db_category = Category(
            name=input.name,
            description=input.description,
            img_url=input.imgUrl
        )
        
        try:
            db.add(db_category)
            db.commit()
            db.refresh(db_category)
            
            return CategoryType(
                id=db_category.id,
                name=db_category.name,
                description=db_category.description,
                imgUrl=db_category.img_url
            )
        except Exception as e:
            db.rollback()
            raise Exception(f"Failed to create category: {str(e)}")

    @strawberry.mutation
    async def update_category(
        self,
        id: int,
        input: UpdateCategoryInput
    ) -> CategoryType:
        db = next(get_db())
        
        # Get existing category
        db_category = db.query(Category).filter(Category.id == id).first()
        if not db_category:
            raise Exception(f"Category with id {id} not found")
        
        # Update fields if provided
        if input.name is not None:
            db_category.name = input.name
        if input.description is not None:
            db_category.description = input.description
        if input.imgUrl is not None:
            db_category.img_url = input.imgUrl
        
        try:
            db.commit()
            db.refresh(db_category)
            
            return CategoryType(
                id=db_category.id,
                name=db_category.name,
                description=db_category.description,
                imgUrl=db_category.img_url
            )
        except Exception as e:
            db.rollback()
            raise Exception(f"Failed to update category: {str(e)}") 