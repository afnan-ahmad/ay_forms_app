from core import ma
from models import User, Form

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


class CreateFormSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Form
        load_instance = True

    title = ma.auto_field()
    description = ma.auto_field()
    fields = ma.auto_field()

    
user_schema = UserSchema()
forms_schema = FormSchema(many=True)
form_schema = FormSchema()
create_form_schema = CreateFormSchema()
