from infra.db.inmemory.mappers.user_inmemory_mapper import UserInMemoryMapper
from infra.db.inmemory.repositories.user_inmemory_repository import UserInMemoryRepository
from infra.db.inmemory.data.user_db import user_db
from shared.dto.mappers.user_dto_mapper import UserDTOMapper
from services.user_service import UserService

_user_db_mapper = UserInMemoryMapper()
_user_repository = UserInMemoryRepository(database=user_db, mapper=_user_db_mapper)

_user_service = UserService(repository=_user_repository)
_user_dto_mapper = UserDTOMapper()

user_module = {
    "service": _user_service,
    "dto_mapper": _user_dto_mapper,
}