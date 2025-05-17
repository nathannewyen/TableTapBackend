import strawberry
from sqlalchemy.orm import Session
from app.models.restaurant import Restaurant
from app.graphql.types.restaurant import RestaurantType, CreateRestaurantInput, UpdateRestaurantInput
from app.db.database import get_db
from typing import List

@strawberry.type
class RestaurantMutation:
    @strawberry.mutation
    def create_restaurant(self, input: CreateRestaurantInput) -> RestaurantType:
        db = next(get_db())
        
        # Check if restaurant already exists
        if db.query(Restaurant).filter(Restaurant.name == input.name).first():
            raise Exception("Restaurant with this name already exists")
        
        # Create new restaurant
        db_restaurant = Restaurant(
            name=input.name,
            address=input.address,
            phone=input.phone,
            email=input.email
        )
        
        try:
            db.add(db_restaurant)
            db.commit()
            db.refresh(db_restaurant)
            
            return RestaurantType(
                id=db_restaurant.id,
                name=db_restaurant.name,
                address=db_restaurant.address,
                phone=db_restaurant.phone,
                email=db_restaurant.email,
                is_active=db_restaurant.is_active,
                categories=[]
            )
        except Exception as e:
            db.rollback()
            raise Exception(f"Failed to create restaurant: {str(e)}")

    @strawberry.mutation
    def update_restaurant(
        self,
        id: int,
        input: UpdateRestaurantInput
    ) -> RestaurantType:
        db = next(get_db())
        
        # Get existing restaurant
        db_restaurant = db.query(Restaurant).filter(Restaurant.id == id).first()
        if not db_restaurant:
            raise Exception(f"Restaurant with id {id} not found")
        
        # Update fields if provided
        if input.name is not None:
            db_restaurant.name = input.name
        if input.address is not None:
            db_restaurant.address = input.address
        if input.phone is not None:
            db_restaurant.phone = input.phone
        if input.email is not None:
            db_restaurant.email = input.email
        if input.is_active is not None:
            db_restaurant.is_active = input.is_active
        
        try:
            db.commit()
            db.refresh(db_restaurant)
            
            return RestaurantType(
                id=db_restaurant.id,
                name=db_restaurant.name,
                address=db_restaurant.address,
                phone=db_restaurant.phone,
                email=db_restaurant.email,
                is_active=db_restaurant.is_active,
                categories=[]
            )
        except Exception as e:
            db.rollback()
            raise Exception(f"Failed to update restaurant: {str(e)}") 