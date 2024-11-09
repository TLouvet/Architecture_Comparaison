import { User } from 'src/domain/entities/User';
import { UserRepository } from 'src/domain/repositories/UserRepository';
import { IUserService } from 'src/domain/services/UserService';

export class UserService implements IUserService {
  constructor(private readonly repository: UserRepository) {}

  async createUser(user: User): Promise<User> {
    return this.repository.add(user);
  }

  async getUserById(userId: number): Promise<User | null> {
    return this.repository.findOne(userId);
  }

  async listAllUsers(): Promise<User[]> {
    return this.repository.findMany();
  }

  async updateUser(userId: number, updatedUser: User): Promise<User | null> {
    return this.repository.update(userId, updatedUser);
  }

  async deleteUser(userId: number): Promise<boolean> {
    return this.repository.delete(userId);
  }
}
