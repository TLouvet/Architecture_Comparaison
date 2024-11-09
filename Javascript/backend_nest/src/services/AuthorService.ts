import { Author } from 'src/domain/entities/Author';
import { AuthorRepository } from 'src/domain/repositories/AuthorRepository';
import { IAuthorService } from 'src/domain/services/IAuthorService';

export class AuthorService implements IAuthorService {
  constructor(private readonly repository: AuthorRepository) {}

  createAuthor(author: Author): Promise<Author> {
    return this.repository.add(author);
  }

  getAuthorById(authorId: number): Promise<Author | null> {
    return this.repository.findOne(authorId);
  }

  listAllAuthors(): Promise<Author[]> {
    return this.repository.findMany();
  }

  updateAuthor(authorId: number, updatedAuthor: Author): Promise<Author | null> {
    return this.repository.update(authorId, updatedAuthor);
  }

  deleteAuthor(authorId: number): Promise<boolean> {
    return this.repository.delete(authorId);
  }
}
