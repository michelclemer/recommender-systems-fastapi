from src.crud.repositories.base import CrudBase
from src.crud.models.users import UserModel


class UsersRepository(CrudBase):
    pass


users_repository = UsersRepository(model=UserModel)