from infra.db.inmemory.mappers.author_inmemory_mapper import AuthorInMemoryMapper
from infra.db.inmemory.repositories.author_inmemory_repository import AuthorInMemoryRepository
from infra.db.inmemory.data.author_db import author_db
from shared.dto.mappers.author_dto_mapper import AuthorDTOMapper
from shared.dto.schemas.author_dto import author_dto
from services.author_service import AuthorService

_author_db_mapper = AuthorInMemoryMapper()
_author_repository = AuthorInMemoryRepository(database=author_db, mapper=_author_db_mapper)

_author_service = AuthorService(repository=_author_repository)
_author_dto_mapper = AuthorDTOMapper()

author_module = {
    "service": _author_service,
    "dto_mapper": _author_dto_mapper,
    "dto_schema": author_dto
}

