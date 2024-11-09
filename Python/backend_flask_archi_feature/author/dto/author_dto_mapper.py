from datetime import datetime
from shared.mapper import BaseMapper
from author.author import Author

class AuthorDTOMapper(BaseMapper[Author, dict]):
    def to_domain(self, dto: dict, author_id: int = 0) -> Author:
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

    def to_external(self, author: Author) -> dict:
        """Transforme un objet domaine Author en dictionnaire DTO."""
        return {
            "id": author.id,
            "first_name": author.first_name,
            "last_name": author.last_name,
            "birth_date": author.birth_date.isoformat(),
            "nationality": author.nationality,
            "death_date": author.death_date.isoformat() if author.death_date else None,
            "biography": author.biography,
            "books": author.books
        }