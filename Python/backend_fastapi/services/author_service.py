from typing import Optional, List
from domain.entities.Author import Author
from domain.repositories.author_repository import AuthorRepository


class AuthorService:
    def __init__(self, repository: AuthorRepository):
        self.repository = repository

    def create_author(self, author: Author) -> Author:
        """Crée un nouvel auteur en ajoutant un objet domaine Author au repository."""
        return self.repository.add_author(author)

    def get_author_by_id(self, author_id: int) -> Optional[Author]:
        """Récupère un auteur par ID en passant par le repository."""
        return self.repository.get_author(author_id)

    def list_all_authors(self) -> List[Author]:
        """Récupère la liste complète des auteurs en utilisant le repository."""
        return self.repository.list_authors()

    def update_author(self, author_id: int, updated_author: Author) -> Optional[Author]:
        """Met à jour un auteur existant en utilisant un objet domaine Author."""
        return self.repository.update_author(author_id, updated_author)

    def delete_author(self, author_id: int) -> bool:
        """Supprime un auteur par ID via le repository."""
        return self.repository.delete_author(author_id)