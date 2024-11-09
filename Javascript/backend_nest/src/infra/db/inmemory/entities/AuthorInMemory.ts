export class AuthorInMemory {
  id: number;
  firstName: string;
  lastName: string;
  birthDate: string;
  nationality: string;
  deathDate: string | null;
  biography?: string;

  constructor(
    id: number,
    firstName: string,
    lastName: string,
    birthDate: string,
    nationality: string,
    deathDate: string | null,
    biography?: string
  ) {
    this.id = id;
    this.firstName = firstName;
    this.lastName = lastName;
    this.birthDate = birthDate;
    this.nationality = nationality;
    this.deathDate = deathDate;
    this.biography = biography;
  }
}
