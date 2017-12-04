import json
import sys

from app import db
from models import Pizza, Choice


def load_catalog(filename):
    
    with open(filename) as file_handler:
        return json.loads(file_handler.read())


if __name__ == '__main__':

    catalog_filename = sys.argv[1] if len(sys.argv) > 1 else 'catalog.json'

    catalog = list()

    for entry in load_catalog(catalog_filename):

        pizza = Pizza(
            title=entry['title'], description=entry['description']
        )

        for choice in entry['choices']:

            pizza.choices.append(
                Choice(
                    title=choice['title'], price=choice['price']
                )
            )

        catalog.append(pizza)

    db.session.add_all(catalog)
    db.session.commit()
    
