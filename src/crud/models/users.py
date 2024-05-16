from sqlmodel import Field, SQLModel


class UserModel(SQLModel, table=True):
    __tablename__ = "users"
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str


class UserRatingMoviesModel(SQLModel, table=True):
    __tablename__ = "user_rating_movies"
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    movie_id: int = Field(foreign_key="movies.id")
    rating: float


class UserWatchedMoviesModel(SQLModel, table=True):
    __tablename__ = "user_watched_movies"
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    movie_id: int = Field(foreign_key="movies.id")
