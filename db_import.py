import json

from app import db
from models import Pizza, Choice


def load_catalog(filename='catalog.json'):
    
    with open(filename) as file_handler:
        return json.loads(file_handler.read())


def create_db_structure():

    db.drop_all()
    db.create_all()


if __name__ == '__main__':

    create_db_structure()

    for entry in load_catalog():

        pizza = Pizza(
            **dict(title=entry['title'], description=entry['description'])
        )

        for choice in entry['choices']:

            pizza.choices.append(
                Choice(
                    **dict(title=choice['title'], price=choice['price'])
                )
            )

        db.session.add(pizza)
        
    db.session.commit()

