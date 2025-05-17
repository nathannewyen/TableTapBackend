from pydantic import BaseModel, Field

class MenuItemCreate(BaseModel):
    name: str = Field(..., example="Margherita Pizza")
    description: str = Field(..., example="Classic pizza with tomatoes, mozzarella, and basil.")
    image: str = Field(..., example="https://cdn/menus/margherita.jpg")
    price: float = Field(..., example=12.99)
    category: str = Field(..., example="Mains")
    available: bool = Field(default=True)