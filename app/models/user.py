from core import db

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, backref

from flask_security.models import fsqla_v3 as fsqla

class User(db.Model, fsqla.FsUserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String, nullable=True)
    active = Column(Boolean)
    
    is_admin = Column(Boolean, default=False)

    roles = relationship('Role', secondary='roles_users', backref=backref('users', lazy='dynamic'))
    forms = relationship('Form', secondary='forms_users', backref=backref('users', lazy='dynamic'))