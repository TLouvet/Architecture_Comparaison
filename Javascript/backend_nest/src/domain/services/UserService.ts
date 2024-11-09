import { User } from 'src/domain/entities/User';

export interface IUserService {
  createUser(user: User): Promise<User>;
  getUserById(userId: number): Promise<User | null>;
  listAllUsers(): Promise<User[]>;
  updateUser(userId: number, updatedUser: User): Promise<User | null>;
  deleteUser(userId: number): Promise<boolean>;
}
