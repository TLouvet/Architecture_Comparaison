from user.db.user_inmemory_mapper import UserInMemoryMapper
from user.db.user_inmemory_repository import UserInMemoryRepository
from user.db.user_db import user_db
from user.dto.user_dto_mapper import UserDTOMapper
from user.dto.user_dto import user_dto
from user.user_service import UserService

_user_db_mapper = UserInMemoryMapper()
_user_repository = UserInMemoryRepository(database=user_db, mapper=_user_db_mapper)

_user_service = UserService(repository=_user_repository)
_user_dto_mapper = UserDTOMapper()

user_module = {
    "service": _user_service,
    "dto_mapper": _user_dto_mapper,
    "dto_schema": user_dto
}