from core import db

from sqlalchemy import Column, Integer, ForeignKey

class FormsUsers(db.Model):
    __tablename__ = 'forms_users'
    id = Column(Integer, primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey('user.id'))
    form_id = Column('form_id', Integer, ForeignKey('form.id'))
