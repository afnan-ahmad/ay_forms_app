from core import db

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.sql import func

class Submission(db.Model):
    __tablename__ = 'submission'
    id = Column(Integer, primary_key=True)
    
    created_at = Column(DateTime, default=func.now())

    form_id = Column(Integer, ForeignKey('form.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    data = Column(JSON, nullable=False)