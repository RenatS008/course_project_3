from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user

api = Namespace('auth')


@api.route('/register/')
class RegisterView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def post(self):
        """
        Create new user.
        """
        if request.json.get('email') and request.json.get('password'):
            new_user = user_service.create(email=request.json.get('email'), password=request.json.get('password'))
            if new_user is not None:
                return f"User: {new_user.email}, {new_user.password}, created", 201
            else:
                return "User creation error", 200


@api.route('/login/')
class LoginView(Resource):
    def post(self):
        """
        login users.
        """
        if request.json.get("email") and request.json.get("password"):
            return user_service.check(email=request.json.get("email"),
                                      password=request.json.get("password")), 200
        else:
            return "logging error", 401

    def put(self):
        """
        Upd token.
        """
        if request.json.get("access_token") and request.json.get("refresh_token"):
            return user_service.update_token(access_token=request.json.get("access_token"),
                                             refresh_token=request.json.get("refresh_token")), 200
        else:
            return "Authorization error", 401
