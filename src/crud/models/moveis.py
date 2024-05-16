from sqlmodel import Field, SQLModel, create_engine, Session, select


class MoviesModel(SQLModel, table=True):
    __tablename__ = "movies"
    id: int = Field(default=None, primary_key=True)
    title: str
    director: str
    genre: str
    year: int


class ActoresModel(SQLModel, table=True):
    __tablename__ = "actores"
    id: int = Field(default=None, primary_key=True)
    name: str
    age: int


class ActorsMoviesModel(SQLModel, table=True):
    __tablename__ = "actors_movies"
    id: int = Field(default=None, primary_key=True)
    actor_id: int = Field(foreign_key="actores.id")
    movie_id: int = Field(foreign_key="movies.id")





