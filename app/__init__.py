from flask import Flask
from flask_wtf.csrf import CSRFProtect # [cite: 209]
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app) # [cite: 211]

from app import views, models