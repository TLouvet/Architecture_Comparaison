from datetime import date
from typing import Dict
from shared.mapper import BaseMapper
from author.author import Author
from author.db.author_inmemory import AuthorInMemory

class AuthorInMemoryMapper(BaseMapper[Author, AuthorInMemory]):
    def to_domain(self, external: AuthorInMemory) -> Author:
        return Author.create(
            id=external.id,
            first_name=external.first_name,
            last_name=external.last_name,
            birth_date=external.birth_date,
            nationality=external.nationality,
            death_date=external.death_date,
            biography=external.biography,
            books=external.books
        )

    def to_external(self, domain: Author) -> AuthorInMemory:        
        return AuthorInMemory(
            id=domain.id,
            first_name=domain.first_name,
            last_name=domain.last_name,
            birth_date=domain.birth_date,
            nationality=domain.nationality,
            death_date=domain.death_date,
            biography=domain.biography,
            books=domain.books
        )