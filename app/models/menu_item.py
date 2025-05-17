from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    img_url = Column(String)
    price = Column(Float, nullable=False)
    category = Column(Integer, ForeignKey("categories.id"))
    available = Column(Boolean, default=True)

    # Relationships
    category_rel = relationship("Category", back_populates="menu_items", foreign_keys=[category])

    def __repr__(self):
        return f"<MenuItem(name='{self.name}', price={self.price})>"        