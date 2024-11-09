import { External } from './External';

/**
 * Le mapper permet de passer d'un objet externe à un objet de domaine et vice-versa.
 * Il sera utilisé pour convertir les DTO et Objets de Base de Données (Externe) en Objet de Domaine.
 * Je suis parti sur une implémentation abstraite afin de fournir une implémentation de base pour les transformations de liste
 * Toutefois chaque implémentation concrète devra fournir une implémentation pour les méthodes toDomain et toExternal
 */
export abstract class Mapper<D, E extends External> {
  abstract toDomain(external: E): D;
  abstract toExternal(domain: D): E;

  toDomainList(externalList: E[]): D[] {
    return externalList.map((external) => this.toDomain(external));
  }

  toExternalList(domainList: D[]): E[] {
    return domainList.map((domain) => this.toExternal(domain));
  }
}
