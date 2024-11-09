import { Author } from 'src/domain/entities/Author';
import { Mapper } from 'src/domain/kernel/Mapper';
import { AuthorInMemory } from '../entities/AuthorInMemory';

export class AuthorInMemoryMapper extends Mapper<Author, AuthorInMemory> {
  toDomain(external: AuthorInMemory): Author {
    return Author.create({
      id: external.id,
      firstName: external.firstName,
      lastName: external.lastName,
      birthDate: new Date(external.birthDate),
      nationality: external.nationality,
      deathDate: external.deathDate ? new Date(external.deathDate) : null,
      biography: external.biography,
      books: [],
    });
  }

  toExternal(domain: Author): AuthorInMemory {
    return new AuthorInMemory(
      domain.id,
      domain.firstName,
      domain.lastName,
      domain.birthDate.toISOString().split('T')[0], // Conversion Date vers string "YYYY-MM-DD"
      domain.nationality,
      domain.deathDate ? domain.deathDate.toISOString().split('T')[0] : null,
      domain.biography
    );
  }
}
