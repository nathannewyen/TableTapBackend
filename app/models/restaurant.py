from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base

class Restaurant(Base):
    __tablename__ = "restaurants"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    address = Column(String(200))
    phone = Column(String(20))
    email = Column(String(100))
    is_active = Column(Boolean, default=True)
    
    # Relationships
    # categories = relationship("Category", back_populates="restaurant") 