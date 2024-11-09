import { User } from '../entities/User';
import { CrudRepository } from '../kernel/RepositoryActions';

export interface UserRepository extends CrudRepository<User> {
  // Ici toute autre méthode qui irait dans un repository d'utilisateur autre que les méthodes CRUD déjà définies
}
