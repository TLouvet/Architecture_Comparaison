from typing import Optional, List
from domain.entities.User import User
from domain.repositories.user_repository import UserRepository

class UserInMemoryRepository(UserRepository):
    def __init__(self, database: dict, mapper):
        self.database = database  # In-memory user database
        self.mapper = mapper
        self.current_id = max(self.database.keys(), default=0) + 1  # Determine next available ID

    def add_user(self, user: User, password: str) -> User:
        """Adds a new user to the database."""
        user_in_memory = self.mapper.to_in_memory(user, password)
        user_in_memory.id = self.current_id
        self.database[self.current_id] = user_in_memory
        self.current_id += 1
        return self.mapper.to_domain(user_in_memory)

    def get_user(self, user_id: int) -> Optional[User]:
        """Retrieves a user by ID and returns it as a domain object."""
        user_in_memory = self.database.get(user_id)
        if user_in_memory:
            return self.mapper.to_domain(user_in_memory)
        return None

    def list_users(self) -> List[User]:
        """Lists all users as domain objects."""
        return [self.mapper.to_domain(user) for user in self.database.values()]

    def update_user(self, user_id: int, updated_user: User) -> Optional[User]:
        """Updates an existing user in the database."""
        if user_id in self.database:
            current_password = self.database[user_id].password
            updated_user.password = current_password # On comprend de cette implémentation que la modification de mdp se fait à part
            user_in_memory = self.mapper.to_in_memory(updated_user)  
            user_in_memory.id = user_id
            self.database[user_id] = user_in_memory
            return self.mapper.to_domain(user_in_memory)
        return None

    def delete_user(self, user_id: int) -> bool:
        """Deletes a user by ID from the database."""
        if user_id in self.database:
            del self.database[user_id]
            return True
        return False