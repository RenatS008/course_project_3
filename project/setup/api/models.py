from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

directors: Model = api.model('Режиссеры', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

movie: Model = api.model('Фильмы', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Название Фильма'),
    'description': fields.String(required=True, max_length=100, example='Описание фильма'),
    'trailer': fields.String(required=True, max_length=100, example='Трейлер фильма'),
    'year': fields.Integer(required=True, max_length=100, example='Год фильма'),
    'rating': fields.Float(required=True, max_length=100, example=10.1),
    'genre': fields.Nested(genre),
    'director': fields.Nested(directors),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='ada@asda.aa'),
    'password': fields.String(required=True, max_length=100, example='asdasd445'),
    'name': fields.String(required=True, max_length=100, example='Nameusers'),
    'surname': fields.String(required=True, max_length=100, example='suranmeUsers'),
    'favorite_genre': fields.Nested(genre),
})

