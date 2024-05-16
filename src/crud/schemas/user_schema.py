from sqlmodel import SQLModel

class UserCreate(SQLModel):
    name: str
    email: str


class UserUpdate(UserCreate):
    pass


class UserInDB(UserCreate):
    id: int
    name: str
    email: str


class User(UserInDB):
    pass


class UserRatingMoviesCreate(SQLModel):
    user_id: int
    movie_id: int
    rating: float


class UserRatingMoviesUpdate(UserRatingMoviesCreate):
    pass


class UserRatingMoviesInDB(UserRatingMoviesCreate):
    id: int
    user_id: int
    movie_id: int
    rating: float


class UserRatingMovies(UserRatingMoviesInDB):
    pass


