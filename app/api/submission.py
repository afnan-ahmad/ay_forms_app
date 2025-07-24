from flask import request
from flask_restful import Resource
from flask_security import auth_required, current_user
from marshmallow import ValidationError
from schemas import submissions_schema, submission_schema, create_submission_schema
from models import Submission, User
from core import db

class SubmissionAPI(Resource):
    @auth_required('token')
    def get(self, form_id):
       user = User.query.filter_by(email=current_user.email).first()
       submissions = None

       if user.is_admin:
           submissions = Submission.query.filter_by(form_id=form_id).all()
       else:
           submissions = Submission.query.filter_by(form_id=form_id).filter_by(user_id=user.id).all()

       return submissions_schema.dump(submissions)

    @auth_required('token')
    def post(self):
       body = request.get_json()
       if not body:
           return 'Submission not provided.'
       
       user = User.query.filter_by(email=current_user.email).first()
       print(user.forms)
       
       try:
           new_submission = create_submission_schema.load(body)
       except ValidationError as err:
           return err.messages, 422
       
       new_submission.user_id = user.id

       db.session.add(new_submission)
       db.session.commit()
    
       return submission_schema.dump(new_submission)

