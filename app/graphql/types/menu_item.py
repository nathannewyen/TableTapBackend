import strawberry
from typing import Optional

@strawberry.type
class MenuItemType:
    id: int
    name: str
    description: Optional[str] = None
    price: float
    imageUrl: Optional[str] = None
    isAvailable: bool = True

@strawberry.input
class MenuItemInput:
    name: str
    description: Optional[str] = None
    price: float
    imageUrl: Optional[str] = None
    isAvailable: bool = True
    categoryId: int

@strawberry.input
class UpdateMenuItemInput:
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    imageUrl: Optional[str] = None
    isAvailable: Optional[bool] = None
    categoryId: Optional[int] = None 