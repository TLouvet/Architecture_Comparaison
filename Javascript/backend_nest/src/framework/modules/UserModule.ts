import { Module } from '@nestjs/common';
import { UserController } from '../controllers/UserController';
import { UserDTOMapper } from 'src/dto/mapper/UserDTOMapper';
import { UserInMemoryMapper } from 'src/infra/db/inmemory/mappers/UserInMemoryMapper';
import { userInMemoryDB } from 'src/infra/db/inmemory/data/UserDB';
import { UserInMemoryRepository } from 'src/infra/db/inmemory/repositories/UserInMemoryRepository';
import { UserRepository } from 'src/domain/repositories/UserRepository';
import { UserService } from 'src/services/UserService';
import { Mapper } from 'src/domain/kernel/Mapper';
import { User } from 'src/domain/entities/User';

@Module({
  imports: [],
  controllers: [UserController],
  providers: [
    {
      provide: 'DTOMapper',
      useClass: UserDTOMapper, // On injecte le mapper pour les DTOs
    },
    {
      provide: 'DatabaseMapper',
      useClass: UserInMemoryMapper, // Le moment où on passe sur autre chose que du inmemory, on peut changer cette ligne pour l'injection
    },
    {
      provide: 'Repository',
      useFactory: (mapper: Mapper<User, any>) => new UserInMemoryRepository(userInMemoryDB, mapper), // Idem ici, on change juste la classe de repository
      inject: ['DatabaseMapper'],
    },
    {
      provide: 'Service',
      useFactory: (authorRepository: UserRepository) => new UserService(authorRepository),
      inject: ['Repository'],
    },
  ],
})
export class UserModule {}
