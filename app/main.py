from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.models import fsqla_v3 as fsqla
from flask_restful import Api
from flask_cors import CORS

from models import User, Role
from core import db, ma
import config

app = Flask(__name__, template_folder='templates')
app.app_context().push()

app.config.from_object(config.DevelopmentConfig())

api = Api(app)
cors = CORS(app)

db.init_app(app)
ma.init_app(app)

fsqla.FsModels.set_db_info(db)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

from api import UserAPI, FormAPI, ExtractionAPI

api.add_resource(UserAPI, '/api/user')
api.add_resource(FormAPI, '/api/forms', '/api/forms/<int:form_id>')
api.add_resource(ExtractionAPI, '/api/extract')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)