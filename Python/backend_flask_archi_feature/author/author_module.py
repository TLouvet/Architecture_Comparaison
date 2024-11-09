from author.db.author_inmemory_mapper import AuthorInMemoryMapper
from author.db.author_inmemory_repository import AuthorInMemoryRepository
from author.db.author_db import author_db
from author.dto.author_dto_mapper import AuthorDTOMapper
from author.dto.author_dto import author_dto
from author.author_service import AuthorService

_author_db_mapper = AuthorInMemoryMapper()
_author_repository = AuthorInMemoryRepository(database=author_db, mapper=_author_db_mapper)

_author_service = AuthorService(repository=_author_repository)
_author_dto_mapper = AuthorDTOMapper()

author_module = {
    "service": _author_service,
    "dto_mapper": _author_dto_mapper,
    "dto_schema": author_dto
}

