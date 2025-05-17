import strawberry
from typing import Optional, List
from .menu_item import MenuItemType

@strawberry.type
class CategoryType:
    id: int
    name: str
    description: Optional[str] = None
    imgUrl: Optional[str] = None
    menuItems: List[MenuItemType] = strawberry.field(default_factory=list)

@strawberry.input
class CategoryInput:
    name: str
    description: Optional[str] = None
    imgUrl: Optional[str] = None
    
@strawberry.input
class UpdateCategoryInput:
    name: Optional[str] = None
    description: Optional[str] = None
    imgUrl: Optional[str] = None