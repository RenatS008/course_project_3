from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user
from project.tools.security import open_token

api = Namespace('user')


@api.route('/')
class UserView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get user by email
        """
        return user_service.get_user_by_token(open_token)

    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def patch(self):
        """
        Patch data users .
        """
        return user_service.update_data_user(data=request.json, token=open_token)


@api.route('/password/')
class PasswordView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def put(self):
        """
        Upd pass user.
        """
        return user_service.update_password_user(data=request.json, token=open_token)

