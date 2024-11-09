import { Module } from '@nestjs/common';
import { AuthorController } from '../controllers/AuthorController';
import { AuthorService } from 'src/services/AuthorService';
import { AuthorRepository } from 'src/domain/repositories/AuthorRepository';
import { AuthorInMemoryMapper } from 'src/infra/db/inmemory/mappers/AuthorInMemoryMapper';
import { AuthorInMemoryRepository } from 'src/infra/db/inmemory/repositories/AuthorInMemoryRepository';
import { AuthorinMemoryDB } from 'src/infra/db/inmemory/data/AuthorDB';
import { AuthorDTOMapper } from 'src/dto/mapper/AuthorDTOMapper';
import { Mapper } from 'src/domain/kernel/Mapper';
import { Author } from 'src/domain/entities/Author';

@Module({
  imports: [],
  controllers: [AuthorController],
  providers: [
    {
      provide: 'DTOMapper',
      useClass: AuthorDTOMapper, // On injecte le mapper pour les DTOs
    },
    {
      provide: 'DatabaseMapper',
      useClass: AuthorInMemoryMapper, // Le moment où on passe sur autre chose que du inmemory, on peut changer cette ligne pour l'injection
    },
    {
      provide: 'Repository',
      useFactory: (mapper: Mapper<Author, any>) => new AuthorInMemoryRepository(AuthorinMemoryDB, mapper), // Idem ici, on change juste la classe de repository
      inject: ['DatabaseMapper'],
    },
    {
      provide: 'Service',
      useFactory: (authorRepository: AuthorRepository) => new AuthorService(authorRepository), // Ici on pourrait décider d'utiliser un autre service
      inject: ['Repository'],
    },
  ],
})
export class AuthorModule {}
