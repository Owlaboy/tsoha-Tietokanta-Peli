from app import app
from flask_sqlalchemy import SQLAlchemy
from secretInfo import DB_URL

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
db = SQLAlchemy(app)