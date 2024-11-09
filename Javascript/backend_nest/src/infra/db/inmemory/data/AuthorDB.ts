import { AuthorInMemory } from '../entities/AuthorInMemory';

export const AuthorinMemoryDB: Record<number, AuthorInMemory> = {
  1: new AuthorInMemory(
    1,
    'Victor',
    'Hugo',
    '1802-02-26',
    'Français',
    '1885-05-22',
    'Poète, romancier et dramaturge, célèbre pour Les Misérables.'
  ),
  2: new AuthorInMemory(
    2,
    'Jane',
    'Austen',
    '1775-12-16',
    'Anglais',
    '1817-07-18',
    'Romancière britannique célèbre pour Orgueil et Préjugés.'
  ),
  3: new AuthorInMemory(
    3,
    'Mark',
    'Twain',
    '1835-11-30',
    'Américain',
    '1910-04-21',
    'Écrivain américain connu pour Les Aventures de Tom Sawyer.'
  ),
  4: new AuthorInMemory(
    4,
    'Gabriel',
    'García Márquez',
    '1927-03-06',
    'Colombien',
    '2014-04-17',
    'Écrivain colombien, prix Nobel de littérature, célèbre pour Cent ans de solitude.'
  ),
  5: new AuthorInMemory(
    5,
    'Mary',
    'Shelley',
    '1797-08-30',
    'Anglais',
    '1851-02-01',
    'Romancière britannique, célèbre pour Frankenstein.'
  ),
};
