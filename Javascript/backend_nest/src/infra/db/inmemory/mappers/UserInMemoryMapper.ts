import { User } from 'src/domain/entities/User';
import { Mapper } from 'src/domain/kernel/Mapper';
import { UserInMemory } from '../entities/UserInMemory';

export class UserInMemoryMapper extends Mapper<User, UserInMemory> {
  toDomain(external: UserInMemory): User {
    return User.create({
      id: external.id,
      email: external.email,
      role: external.role,
      firstName: external.firstName,
      lastName: external.lastName,
    });
  }

  toExternal(domain: User): UserInMemory {
    return new UserInMemory(domain.id, domain.email, domain.role, domain.firstName, domain.lastName);
  }
}
