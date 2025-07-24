from core import db

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.sqlite import JSON

class Form(db.Model):
    __tablename__ = 'form'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(100))
    fields = Column(JSON, nullable=False)
