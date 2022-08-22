from project.dao import GenresDAO
from project.dao import MoviesDAO
from project.dao import DirectorsDAO
from project.dao import UsersDAO

from project.services import MoviesService
from project.services import DirectorsService
from project.services import GenresService
from project.services import UsersService

from project.setup.db import db

movie_service = MoviesService(dao=MoviesDAO(db.session))
director_service = DirectorsService(dao=DirectorsDAO(db.session))
genre_service = GenresService(dao=GenresDAO(db.session))
user_service = UsersService(dao=UsersDAO(db.session))
