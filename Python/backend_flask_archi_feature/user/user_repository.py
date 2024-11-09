from abc import ABC, abstractmethod
from typing import List, Optional
from user.user import User

# Cette classe ne va pas dans DB car elle représente un contrat entre le domaine et la couche de données
class UserRepository(ABC):
    @abstractmethod
    def add_user(self, user: User) -> User:
        """Ajoute un auteur et retourne l'objet domaine."""
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> Optional[User]:
        """Récupère un auteur par son ID et retourne l'objet domaine."""
        pass

    @abstractmethod
    def list_users(self) -> List[User]:
        """Retourne une liste de tous les auteurs sous forme d'objets domaine."""
        pass

    @abstractmethod
    def update_user(self, user_id: int, updated_user: User) -> Optional[User]:
        """Met à jour un auteur existant et retourne l'objet domaine mis à jour."""
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        """Supprime un auteur par son ID et retourne True si l'opération a réussi."""
        pass