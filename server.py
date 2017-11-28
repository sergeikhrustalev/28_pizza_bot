from os import getenv
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import request, Response
from werkzeug.exceptions import HTTPException

from app import app, db
from models import Pizza, Choice


class AuthException(HTTPException):

    def __init__(self, message):

        super().__init__(

            message, Response(
                "You could not be authenticated. Please refresh the page.",
                http_responce_code,
                {'WWW-Authenticate': 'Basic realm="Login Required"'}
            )

        )


class CustomModelView(ModelView):

    @staticmethod
    def check_auth(username, password):
        return username == getenv('ADMIN_LOGIN') and password == getenv('ADMIN_PASSWORD')

    def is_accessible(self):

        auth = request.authorization

        if not auth or not self.check_auth(auth.username, auth.password):
            raise AuthException('Not authenticated')

        return True


if __name__ == '__main__':
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    admin = Admin(app, template_mode='bootstrap3')
    admin.add_view(CustomModelView(Pizza, db.session))
    admin.add_view(CustomModelView(Choice, db.session))
    app.run()
