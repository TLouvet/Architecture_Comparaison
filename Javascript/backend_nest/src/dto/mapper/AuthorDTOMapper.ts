import { Author } from 'src/domain/entities/Author';
import { AuthorDTO } from '../schema/AuthorDTO';
import { Mapper } from 'src/domain/kernel/Mapper';

export class AuthorDTOMapper extends Mapper<Author, AuthorDTO> {
  toDomain(external: AuthorDTO): Author {
    return Author.create({
      id: external?.id || null,
      firstName: external.firstName,
      lastName: external.lastName,
      birthDate: new Date(external.birthDate),
      nationality: external.nationality,
      deathDate: external.deathDate ? new Date(external.deathDate) : null,
      biography: external.biography,
      books: external.books || [],
    });
  }

  toExternal(domain: Author): AuthorDTO {
    return {
      id: domain.id,
      firstName: domain.firstName,
      lastName: domain.lastName,
      birthDate: domain.birthDate.toISOString().split('T')[0],
      nationality: domain.nationality,
      deathDate: domain.deathDate ? domain.deathDate.toISOString().split('T')[0] : null,
      biography: domain.biography,
      books: domain.books,
    };
  }
}
