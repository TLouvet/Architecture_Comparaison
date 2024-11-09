interface AuthorInput {
  id: number;
  firstName: string;
  lastName: string;
  birthDate: Date;
  nationality: string;
  deathDate: Date | null;
  biography?: string;
  books?: number[];
}

export class Author {
  private static readonly ALLOWED_NATIONALITIES = new Set([
    'Français',
    'Anglais',
    'Américain',
    'Espagnol',
    'Allemand',
    'Colombien',
  ]);

  private _id: number;
  private _firstName: string;
  private _lastName: string;
  private _birthDate: Date;
  private _nationality: string;
  private _deathDate: Date | null;
  private _biography?: string;
  private _books: number[];

  constructor(input: AuthorInput) {
    const { id, firstName, lastName, birthDate, deathDate, nationality, biography, books } = input;

    this._id = id;
    this._firstName = firstName;
    this._lastName = lastName;
    this._birthDate = birthDate;
    this._nationality = nationality;
    this._deathDate = deathDate;
    this._biography = biography;
    this._books = books;
  }

  static create(input: AuthorInput): Author {
    const { nationality, deathDate, birthDate } = input;
    if (!Author.ALLOWED_NATIONALITIES.has(nationality)) {
      throw new Error(
        `Nationalité '${nationality}' non reconnue. Les nationalités acceptées sont : ${Array.from(
          Author.ALLOWED_NATIONALITIES
        ).join(', ')}`
      );
    }

    if (deathDate && birthDate >= deathDate) {
      throw new Error('La date de naissance doit être antérieure à la date de décès.');
    }

    return new Author(input);
  }

  setId(id: number): void {
    this._id = id;
  }

  get id(): number {
    return this._id;
  }

  get firstName(): string {
    return this._firstName;
  }

  get lastName(): string {
    return this._lastName;
  }

  get birthDate(): Date {
    return this._birthDate;
  }

  get nationality(): string {
    return this._nationality;
  }

  get deathDate(): Date | null {
    return this._deathDate;
  }

  get biography(): string | undefined {
    return this._biography;
  }

  get books(): number[] {
    return this._books;
  }
}
