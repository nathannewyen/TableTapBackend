import strawberry
from typing import Optional, List
from .category import CategoryType

@strawberry.type
class RestaurantType:
    id: int
    name: str
    address: str
    phone: str
    email: str
    is_active: bool
    categories: List[CategoryType]

@strawberry.input
class CreateRestaurantInput:
    name: str
    address: str
    phone: str
    email: str

@strawberry.input
class UpdateRestaurantInput:
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None 