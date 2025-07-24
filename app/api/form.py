from flask import request
from flask_restful import Resource
from flask_security import auth_required, current_user
from marshmallow import ValidationError
from schemas import forms_schema, form_schema, create_form_schema
from models import Form, User
from core import db

class FormAPI(Resource):
    @auth_required('token')
    def get(self):
       user = User.query.filter_by(email=current_user.email).first()
       if user.is_admin:
           forms = Form.query.all()
           return forms_schema.dump(forms)
       
       return forms_schema.dump(user.forms)

    @auth_required('token')
    def post(self):
       body = request.get_json()
       if not body:
           return 'Form not provided.'
       
       user = User.query.filter_by(email=current_user.email).first()
       if not user.is_admin:
           return 'Only admin can create forms.', 400
       
       try:
           new_form = create_form_schema.load(body)
       except ValidationError as err:
           return err.messages, 422
       
       new_form.users.append(user)
       
       db.session.add(new_form)
       db.session.commit()
       
       return form_schema.dump(new_form)

