from fastapi import APIRouter, HTTPException
from sqlmodel import Session
from typing import List
from src.api.deps import SessionDep
from src.crud.repositories.moveis import movies_repository, actors_movies_repository, actores_repository
from src.crud.schemas.moveis_schema import MoviesCreate, ActorsMoviesCreate, ActorsCreate

router = APIRouter()


@router.post("/register/")
async def register_moveis(session: SessionDep, movie: MoviesCreate):
    movie_data = movies_repository.filter_by(db=session, filter_data={"title": movie.title})
    if movie_data:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    movies_repository.create(db=session, obj_in=movie)
    return {"message": "Movies registered successfully!"}

@router.get("/list-movies/")
async def get_all_movies(session: SessionDep, skip: int = 0, limit: int = 100):
    movies = movies_repository.get_multi(session, skip=skip, limit=limit)
    return movies

@router.get("/list-movies/{movie_id}/", response_model=dict)
async def get_movie_by_id(session: SessionDep, movie_id: int):
    movie = movies_repository.get(session, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie.dict()

@router.post("/actors/")
async def register_actors_movies(session: SessionDep, actor: ActorsCreate):
    actores_repository.create(db=session, obj_in=actor)
    return {"message": "Actors registered successfully!"}

@router.get("/actors/list/")
async def get_all_actors(session: SessionDep, skip: int = 0, limit: int = 100):
    actors = actores_repository.get_multi(session, skip=skip, limit=limit)
    return actors

@router.post("/actors-movies/")
async def register_actors_movies(session: SessionDep, actor_movie: ActorsMoviesCreate):
    actors_movies_repository.create(db=session, obj_in=actor_movie)
    return {"message": "Actors Movies registered successfully!"}

@router.get("/actors-movies/list/")
async def get_all_actors_movies(session: SessionDep, skip: int = 0, limit: int = 100):
    actors_movies = actors_movies_repository.get_multi(session, skip=skip, limit=limit)
    return actors_movies

@router.get("/actors-movies/list/{actor_movie_id}/", response_model=dict)
async def get_actors_movies_by_id(session: SessionDep, actor_movie_id: int):
    actors_movies = actors_movies_repository.get(session, actor_movie_id)
    if not actors_movies:
        raise HTTPException(status_code=404, detail="Actors Movies not found")
    return actors_movies.dict()


