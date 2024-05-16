from src.crud.repositories.base import CrudBase
from src.crud.models.moveis import MoviesModel, ActorsMoviesModel, ActoresModel


class MoviesRepository(CrudBase):
    pass


movies_repository = MoviesRepository(model=MoviesModel)
actors_movies_repository = MoviesRepository(model=ActorsMoviesModel)
actores_repository = MoviesRepository(model=ActoresModel)
