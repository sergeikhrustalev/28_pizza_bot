from app import db
from models import Pizza, Choice


db.drop_all()
db.create_all()
