from sqlalchemy import Column, Integer, String
from app.database import Base

class Item(Base):
    __tablename__ = "itens"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    last_name = Column(String(50), unique=True, index=True, nullable=False)
    college_course = Column(String(50), unique=True, index=True, nullable=False)
    