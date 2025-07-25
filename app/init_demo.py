from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.models import fsqla_v3 as fsqla
from secrets import token_urlsafe, SystemRandom
from dotenv import set_key
from pathlib import Path
import os

from models import User, Role
from core import db
import config

app = Flask(__name__, template_folder='templates')
app.app_context().push()

app.config.from_object(config.DevelopmentConfig())

db.init_app(app)

fsqla.FsModels.set_db_info(db)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

DEMO_ADMIN_EMAIL = 'admin@test.com'
DEMO_ADMIN_PASSWORD = 'Test@123'
DEMO_USER_EMAIL = 'user@test.com'
DEMO_USER_PASSWORD = 'Test@123'

with app.app_context():
    db.create_all()
    
    admin = user_datastore.create_user(
        email=DEMO_ADMIN_EMAIL,
        password=DEMO_ADMIN_PASSWORD,
        active=True,
        is_admin=True
    )
    user = user_datastore.create_user(
            email=DEMO_USER_EMAIL,
            password=DEMO_USER_PASSWORD,
            active=True
    )

    db.session.commit()

    test_env_file = Path(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../.env'))
    test_env_file.touch(0o600, exist_ok=False)

    set_key(dotenv_path=test_env_file, key_to_set='SECURITY_PASSWORD_SALT', value_to_set=str(SystemRandom().getrandbits(128)))
    set_key(dotenv_path=test_env_file, key_to_set='SECRET_KEY', value_to_set=token_urlsafe(128))

    print(f"Demo database initialized successfully.")