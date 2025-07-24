from flask_restful import Resource
from flask_security import auth_required, current_user
from schemas import user_schema
from models import User

class UserAPI(Resource):
    @auth_required('token')
    def get(self):
       user = User.query.filter_by(email=current_user.email).first()
       return user_schema.dump(user)
