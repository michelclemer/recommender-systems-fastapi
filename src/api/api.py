from fastapi import APIRouter

from .routers import movies, users

router = APIRouter()

router.include_router(movies.router)
router.include_router(users.router)

