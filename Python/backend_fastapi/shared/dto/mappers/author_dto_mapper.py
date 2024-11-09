from datetime import datetime
from domain.kernel.Mapper import BaseMapper
from domain.entities.Author import Author
from shared.dto.schemas.author_dto import AuthorDTO

class AuthorDTOMapper(BaseMapper[Author, AuthorDTO]):
    def to_domain(self, dto: AuthorDTO, author_id: int = 0) -> Author:
        """Transforme un dictionnaire DTO en objet domaine Author."""
        return Author.create(
            id=author_id,
            first_name=dto["first_name"],
            last_name=dto["last_name"],
            birth_date=datetime.strptime(dto["birth_date"], "%Y-%m-%d").date(),
            nationality=dto.get("nationality"),
            death_date=datetime.strptime(dto["death_date"], "%Y-%m-%d").date() if dto.get("death_date") else None,
            biography=dto.get("biography"),
            books=dto.get("books", [])
        )

    def to_external(self, author: Author) -> AuthorDTO:
        """Transforme un objet domaine Author en dictionnaire DTO."""
        return AuthorDTO(
            first_name=author.first_name,
            last_name=author.last_name,
            birth_date=author.birth_date.isoformat(),
            nationality=author.nationality,
            death_date=author.death_date.isoformat() if author.death_date else None,
            biography=author.biography,
            books=author.books
        )