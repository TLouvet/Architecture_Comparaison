from typing import Optional, List
from user.user import User
from user.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.repository.get_user(user_id)

    def list_all_users(self) -> List[User]:
        return self.repository.list_users()

    def update_user(self, user_id: int, updated_user: User) -> Optional[User]:
        return self.repository.update_user(user_id, updated_user)

    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete_user(user_id)