from core import db

from sqlalchemy import Column, Integer, String

from flask_security.models import fsqla_v3 as fsqla

class Role(db.Model, fsqla.FsRoleMixin):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    description = Column(String(255))