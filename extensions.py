from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_redis import FlaskRedis

# Initializing the objects
bcrypt = Bcrypt()
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
# redis_store = FlaskRedis()