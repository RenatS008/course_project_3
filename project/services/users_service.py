from typing import Optional, List

from project.dao import UsersDAO
from project.tools.security import generate_password_hash, update_token, generate_token, get_user_by_token
from project.exceptions import ItemNotFound
from project.models import User


class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    """
    METHODS GETS
    """

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> List[User]:
        return self.dao.get_all(page=page)

    def get_by_email(self, email) -> User:
        return self.dao.get_by_email(email=email)

    def get_user_by_token(self, token):
        data = get_user_by_token(token)
        if data:
            return self.get_by_email(data.get("email"))

    """
    METHODS CREATE
    """

    def create(self, email, password):
        return self.dao.create(email=email, password=generate_password_hash(password))

    """
    METHODS UPDATE
    """

    def update_token(self, access_token, refresh_token):
        return update_token(refresh_token=refresh_token)

    def update_data_user(self, token, data):
        new_data = get_user_by_token(token)
        if new_data:
            self.dao.update_data(data=data, email=new_data.get("email"))
        return self.get_by_email(new_data.get("email"))

    def update_password_user(self, data, token):
        new_pass = get_user_by_token(token)
        if data:
            self.dao.update_data(
                data={
                    "password": generate_password_hash(data.get("password_2"))
                    },
                email=new_pass.get("email")
            )
            return self.get_by_email(new_pass.get("email"))

    """
    METHODS CHECK
    """

    def check(self, email, password):
        user = self.get_by_email(email)
        return generate_token(email=email, password=password, password_hash=user.password)
