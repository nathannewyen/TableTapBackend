from typing import List, Optional
from pydantic import BaseModel, Field

# Category schemas
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    name: Optional[str] = None

class Category(CategoryBase):
    id: int
    
    class Config:
        from_attributes = True

# Menu Item schemas
class MenuItemCustomizationBase(BaseModel):
    name: str
    options: str  # JSON stored as string
    additional_price: float = Field(ge=0)

class MenuItemCustomizationCreate(MenuItemCustomizationBase):
    pass

class MenuItemCustomization(MenuItemCustomizationBase):
    id: int
    menu_item_id: int
    
    class Config:
        from_attributes = True

class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(ge=0)
    image_url: Optional[str] = None
    is_available: bool = True
    category_id: int

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Field(None, ge=0)
    image_url: Optional[str] = None
    is_available: Optional[bool] = None
    category_id: Optional[int] = None

class MenuItem(MenuItemBase):
    id: int
    customizations: List[MenuItemCustomization] = []
    
    class Config:
        from_attributes = True

class MenuItemDetail(MenuItem):
    category: Category
    
    class Config:
        from_attributes = True