from sqlmodel import Session
from sqlalchemy.future import select
from src.crud.models.moveis import MoviesModel, ActorsMoviesModel, ActoresModel
from src.crud.models.users import UserWatchedMoviesModel, UserRatingMoviesModel

def generate_recommendations(usuario_id: int, session: Session):

    watched_movies_stmt = select(UserWatchedMoviesModel).where(UserWatchedMoviesModel.user_id == usuario_id)
    watched_movies_result = session.execute(watched_movies_stmt)
    watched_movies_ids = [record.movie_id for record in watched_movies_result.scalars().all()]

    rated_movies_stmt = select(UserRatingMoviesModel).where(UserRatingMoviesModel.user_id == usuario_id)
    rated_movies_result = session.execute(rated_movies_stmt)
    rated_movies_ids = [record.movie_id for record in rated_movies_result.scalars().all()]
    rated_movies_dict = {record.movie_id: record.rating for record in rated_movies_result.scalars().all()}


    movies_info_stmt = select(MoviesModel).where(MoviesModel.id.in_(watched_movies_ids + rated_movies_ids))
    movies_info_result = session.execute(movies_info_stmt)
    movies_info = movies_info_result.scalars().all()

    genres = set()
    directors = set()
    actors = set()

    for movie in movies_info:
        genres.add(movie.genre)
        directors.add(movie.director)

        actors_movies_stmt = select(ActorsMoviesModel).where(ActorsMoviesModel.movie_id == movie.id)
        actors_movies_result = session.execute(actors_movies_stmt)
        actor_ids = [record.actor_id for record in actors_movies_result.scalars().all()]

        actors_stmt = select(ActoresModel).where(ActoresModel.id.in_(actor_ids))
        actors_result = session.execute(actors_stmt)
        actors.update([actor.name for actor in actors_result.scalars().all()])

    recommendations_stmt = select(MoviesModel).where(
        MoviesModel.genre.in_(genres) |
        MoviesModel.director.in_(directors) |
        MoviesModel.id.in_(
            select(ActorsMoviesModel.movie_id).where(
                ActorsMoviesModel.actor_id.in_(
                    select(ActoresModel.id).where(ActoresModel.name.in_(actors))
                )
            )
        )
    ).order_by(MoviesModel.year.desc()).limit(10)

    recommendations_result = session.execute(recommendations_stmt)
    recommendations = recommendations_result.scalars().all()

    return recommendations
