from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.menu_item import MenuItem

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(String(200), nullable=True)
    
    # Remove menu_items relationship if not needed, or update to string if needed elsewhere
    # menu_items = relationship("MenuItem", back_populates="category")
    

# Removed duplicate MenuItem class

class MenuItemCustomization(Base):
    __tablename__ = "menu_item_customizations"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    options = Column(String(500))  # JSON stored as string
    additional_price = Column(Float, default=0.0)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))
    
    # Remove menu_item relationship if not needed, or update to string if needed elsewhere
    # menu_item = relationship("MenuItem", back_populates="customizations")