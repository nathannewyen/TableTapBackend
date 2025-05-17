from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    image = Column(String)
    price = Column(Float, nullable=False)
    category = Column(String)
    available = Column(Boolean, default=True)

    def __repr__(self):
        return f"<MenuItem(name='{self.name}', price={self.price})>"        