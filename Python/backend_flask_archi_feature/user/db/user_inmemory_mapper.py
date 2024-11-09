from user.user import User
from user.db.user_inmemory import UserInMemory
from shared.mapper import BaseMapper

class UserInMemoryMapper(BaseMapper[User, UserInMemory]):
    def to_domain(self, user_in_memory: UserInMemory) -> User:
        return User.create(
            id=user_in_memory.id,
            email=user_in_memory.email,
            role=user_in_memory.role,
            first_name=user_in_memory.first_name,
            last_name=user_in_memory.last_name
        )

    def to_external(self, user: User) -> UserInMemory:
        return UserInMemory(
            id=user.id,
            email=user.email,
            password=user.password,
            role=user.role,
            first_name=user.first_name,
            last_name=user.last_name
        )