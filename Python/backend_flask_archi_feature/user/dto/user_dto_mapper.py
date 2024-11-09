from user.user import User
from shared.mapper import BaseMapper

class UserDTOMapper(BaseMapper[User, dict]):
    def to_domain(self, dto: dict, user_id: int = 0) -> User:
        return User.create(
            id=user_id,
            email=dto["email"],
            role=dto["role"],
            first_name=dto["first_name"],
            last_name=dto["last_name"]
        )

    # Notez qu'on décide dans le mapper de ne pas retourner le mot de passe de l'utilisateur au front-end
    def to_external(self, user: User) -> dict:
        return {
            "id": user.id,
            "email": user.email,
            "role": user.role,
            "first_name": user.first_name,
            "last_name": user.last_name
        }