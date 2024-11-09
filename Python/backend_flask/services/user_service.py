from typing import Optional, List
from domain.entities.User import User
from domain.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.repository.get_user(user_id)

    def list_all_users(self) -> List[User]:
        return self.repository.list_users()

    def update_user(self, user_id: int, updated_user: User) -> Optional[User]:
        return self.repository.update_user(user_id, updated_user)

    # TODO: Ici on doit retravailler le service de manière à ce que seul un super admin puisse supprimer un utilisateur admin
    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete_user(user_id)