from typing import Optional, List, Dict
from author.author import Author
from author.author_repository import AuthorRepository
from author.db.author_inmemory import AuthorInMemory
from shared.mapper import BaseMapper


class AuthorInMemoryRepository(AuthorRepository):
    def __init__(self, database: Dict[int, AuthorInMemory], mapper: BaseMapper[Author, AuthorInMemory]):
        self.database = database 
        self.current_id = max(self.database.keys(), default=0) + 1 
        self.mapper = mapper

    def list_authors(self) -> List[Author]:
        """Liste tous les auteurs sous forme d'objets domaine."""
        return self.mapper.to_domain_list(self.database.values())

    def get_author(self, author_id: int) -> Optional[Author]:
        """Récupère un auteur par ID et le convertit en objet domaine."""
        author_in_memory = self.database.get(author_id)
        if author_in_memory:
            return self.mapper.to_domain(author_in_memory)
        return None

    def add_author(self, author: Author) -> Author:
        """Ajoute un auteur en convertissant l'objet domaine en objet de base de données."""
        author_in_memory = self.mapper.to_external(author)
        author_in_memory.id = self.current_id 
        self.database[self.current_id] = author_in_memory
        self.current_id += 1
        return self.mapper.to_domain(author_in_memory)

    def update_author(self, author_id: int, updated_author: Author) -> Optional[Author]:
        """Met à jour un auteur existant avec les données d'un objet domaine."""
        if author_id in self.database:
            author_in_memory = self.mapper.to_external(updated_author)
            author_in_memory.id = author_id
            self.database[author_id] = author_in_memory
            return self.mapper.to_domain(author_in_memory)
        return None

    def delete_author(self, author_id: int) -> bool:
        """Supprime un auteur par ID de la base de données en mémoire."""
        if author_id in self.database:
            del self.database[author_id]
            return True
        return False