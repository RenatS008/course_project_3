from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user
from project.tools.security import open_token

api = Namespace('user')


@api.route('/')
class UserView(Resource):
    @api.marshal_with(user, code=200, description='OK')
    def get(self):
        """
        Get user by email
        """
        token = open_token()
        return user_service.get_user_by_token(token)

    @api.marshal_with(user, code=200, description='OK')
    def patch(self):
        """
        Patch data users .
        """
        token = open_token()
        return user_service.update_data_user(data=request.json, token=token)


@api.route('/password/')
class PasswordView(Resource):
    @api.marshal_with(user, code=200, description='OK')
    def put(self):
        """
        Upd pass user.
        """
        token = open_token()
        return user_service.update_password_user(data=request.json, token=token)

