import { User } from 'src/domain/entities/User';
import { Mapper } from 'src/domain/kernel/Mapper';
import { UserDTO } from '../schema/UserDTO';

export class UserDTOMapper extends Mapper<User, UserDTO> {
  toDomain(external: UserDTO): User {
    return User.create({
      id: external?.id || null,
      email: external.email,
      role: external.role,
      firstName: external.firstName,
      lastName: external.lastName,
    });
  }

  toExternal(domain: User): UserDTO {
    return {
      id: domain.id,
      email: domain.email,
      role: domain.role,
      firstName: domain.firstName,
      lastName: domain.lastName,
    };
  }
}
