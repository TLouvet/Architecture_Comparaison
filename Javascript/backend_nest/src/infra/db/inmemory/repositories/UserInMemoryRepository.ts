import { User } from 'src/domain/entities/User';
import { UserRepository } from 'src/domain/repositories/UserRepository';
import { UserInMemory } from '../entities/UserInMemory';
import { Mapper } from 'src/domain/kernel/Mapper';

export class UserInMemoryRepository implements UserRepository {
  constructor(private readonly db: Record<number, UserInMemory>, private readonly mapper: Mapper<User, UserInMemory>) {}

  async findOne(id: number): Promise<User | null> {
    if (!this.db[id]) {
      return null;
    }
    return this.mapper.toDomain(this.db[id]);
  }

  async findMany(): Promise<User[]> {
    return this.mapper.toDomainList(Object.values(this.db));
  }

  async add(user: User): Promise<User> {
    this.db[user.id] = this.mapper.toExternal(user);
    return user;
  }

  async update(id: number, user: User): Promise<User> {
    if (!this.db[id]) {
      throw new Error(`Utilisateur avec l'identifiant ${id} non trouvé`);
    }
    this.db[id] = this.mapper.toExternal(user);
    return user;
  }

  async delete(id: number): Promise<boolean> {
    if (!this.db[id]) {
      return false;
    }
    delete this.db[id];
    return true;
  }
}
