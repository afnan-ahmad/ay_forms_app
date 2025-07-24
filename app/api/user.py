from flask import request
from flask_restful import Resource
from flask_security import auth_required, current_user
from schemas import user_schema, users_schema
from models import User

class UserAPI(Resource):
    @auth_required('token')
    def get(self):
        user = User.query.filter_by(email=current_user.email).first()
        get_all_users = request.args.get('all_users')

        if user.is_admin and get_all_users:
           users = User.query.all()
           return users_schema.dump(users)
        
        return user_schema.dump(user)
