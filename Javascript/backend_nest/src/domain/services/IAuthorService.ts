import { Author } from 'src/domain/entities/Author';

export interface IAuthorService {
  createAuthor(author: Author): Promise<Author>;
  getAuthorById(authorId: number): Promise<Author | null>;
  listAllAuthors(): Promise<Author[]>;
  updateAuthor(authorId: number, updatedAuthor: Author): Promise<Author | null>;
  deleteAuthor(authorId: number): Promise<boolean>;
}
