from abc import ABC, abstractmethod
from typing import List, Optional
from author.author import Author

# Cette classe ne va pas dans DB car elle représente un contrat entre le domaine et la couche de données
class AuthorRepository(ABC):
    @abstractmethod
    def add_author(self, author: Author) -> Author:
        """Ajoute un auteur et retourne l'objet domaine."""
        pass

    @abstractmethod
    def get_author(self, author_id: int) -> Optional[Author]:
        """Récupère un auteur par son ID et retourne l'objet domaine."""
        pass

    @abstractmethod
    def list_authors(self) -> List[Author]:
        """Retourne une liste de tous les auteurs sous forme d'objets domaine."""
        pass

    @abstractmethod
    def update_author(self, author_id: int, updated_author: Author) -> Optional[Author]:
        """Met à jour un auteur existant et retourne l'objet domaine mis à jour."""
        pass

    @abstractmethod
    def delete_author(self, author_id: int) -> bool:
        """Supprime un auteur par son ID et retourne True si l'opération a réussi."""
        pass