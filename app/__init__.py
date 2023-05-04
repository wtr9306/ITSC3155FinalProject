from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SECRET_KEY'] = '5fcec93ad7e99b9e7e0e80fe9f054565'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models


