from domain.kernel.Mapper import BaseMapper
from domain.entities.User import User
from shared.dto.schemas.user_dto import UserDTO

class UserDTOMapper(BaseMapper[User, UserDTO]):
    def to_domain(self, dto: UserDTO, user_id: int = 0) -> User:
        return User.create(
            id=user_id,
            email=dto["email"],
            role=dto["role"],
            first_name=dto["first_name"],
            last_name=dto["last_name"]
        )

    def to_external(self, user: User) -> UserDTO:
       return UserDTO(
            email=user.email,
            role=user.role,
            first_name=user.first_name,
            last_name=user.last_name
        )