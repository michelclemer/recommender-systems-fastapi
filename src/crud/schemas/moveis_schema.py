from sqlmodel import SQLModel


class MoviesCreate(SQLModel):
    title: str
    director: str
    year: int
    genre: str = None


class MoviesUpdate(SQLModel):
    title: str = None
    director: str = None
    year: int = None


class MoviesRead(MoviesCreate):
    id: int


class ActorsCreate(SQLModel):
    name: str
    age: int


class ActorsUpdate(SQLModel):
    name: str = None
    age: int = None


class ActorsRead(ActorsCreate):
    id: int


class ActorsMoviesCreate(SQLModel):
    actor_id: int
    movie_id: int


class ActorsMoviesRead(ActorsMoviesCreate):
    id: int
