import { Author } from '../entities/Author';
import { CrudRepository } from '../kernel/RepositoryActions';

export interface AuthorRepository extends CrudRepository<Author> {}
