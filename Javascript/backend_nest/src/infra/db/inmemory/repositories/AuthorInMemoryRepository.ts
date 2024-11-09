import { Author } from 'src/domain/entities/Author';
import { AuthorRepository } from 'src/domain/repositories/AuthorRepository';
import { AuthorInMemory } from '../entities/AuthorInMemory';
import { Mapper } from 'src/domain/kernel/Mapper';

export class AuthorInMemoryRepository implements AuthorRepository {
  private maxId: number;
  constructor(
    private readonly db: Record<number, AuthorInMemory>,
    private readonly mapper: Mapper<Author, AuthorInMemory>
  ) {
    this.maxId = db ? Math.max(...Object.keys(db).map(Number)) : 0;
  }

  async findOne(id: number): Promise<Author | null> {
    if (!this.db[id]) {
      return null;
    }

    return this.mapper.toDomain(this.db[id]);
  }

  async findMany(): Promise<Author[]> {
    return this.mapper.toDomainList(Object.values(this.db));
  }

  async add(author: Author): Promise<Author> {
    author.setId(++this.maxId);
    this.db[this.maxId] = this.mapper.toExternal(author);
    return author;
  }

  async update(id: number, author: Author): Promise<Author> {
    if (!this.db[id]) {
      throw new Error(`Auteur avec l'identifiant ${id} non trouvé`);
    }

    this.db[id] = this.mapper.toExternal(author);
    return author;
  }

  async delete(id: number): Promise<boolean> {
    if (!this.db[id]) {
      return false;
    }

    delete this.db[id];
    return true;
  }
}
