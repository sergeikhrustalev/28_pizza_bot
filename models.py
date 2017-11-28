from app import db


class Pizza(db.Model):
    __tablename__ = 'pizza'
    pizza_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(127))
    description = db.Column(db.String(255))
    choices = db.relationship('Choice', backref = 'pizza', lazy = 'dynamic')

class Choice(db.Model):
    __tablename__ = 'choice'
    choice_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(127))
    price = db.Column(db.Integer)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.pizza_id'))

