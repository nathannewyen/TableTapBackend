from pydantic import BaseModel, Field

class MenuItemCreate(BaseModel):
    name: str = Field(..., example="Margherita Pizza")
    description: str = Field(..., example="Classic pizza with tomatoes, mozzarella, and basil.")
    img_url: str = Field(..., example="https://example.com/images/margherita.jpg")
    price: float = Field(..., example=12.99)
    category: str = Field(..., example="Mains")
    available: bool = Field(default=True)