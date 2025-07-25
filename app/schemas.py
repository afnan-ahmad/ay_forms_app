from core import ma
from models import User, Form, Submission

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    email = ma.auto_field()
    name = ma.auto_field()
    is_admin = ma.auto_field()

class FormSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Form
        
class SubmissionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Submission
        include_fk = True

class CreateFormSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Form
        load_instance = True

    title = ma.auto_field()
    description = ma.auto_field()
    fields = ma.auto_field()
    users = ma.auto_field()

class CreateSubmissionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Submission
        load_instance = True

    form_id = ma.auto_field()
    data = ma.auto_field()

users_schema = UserSchema(many=True)
user_schema = UserSchema()
forms_schema = FormSchema(many=True)
form_schema = FormSchema()
submissions_schema = SubmissionSchema(many=True)
submission_schema = SubmissionSchema()

create_form_schema = CreateFormSchema()
create_submission_schema = CreateSubmissionSchema()