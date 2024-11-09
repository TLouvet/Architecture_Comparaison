import { UserInMemory } from '../entities/UserInMemory';

export const userInMemoryDB: Record<number, UserInMemory> = {
  1: new UserInMemory(1, 'admin@example.com', 'admin', 'Admin', 'User'),
  2: new UserInMemory(2, 'reader@example.com', 'reader', 'Reader', 'User'),
};
