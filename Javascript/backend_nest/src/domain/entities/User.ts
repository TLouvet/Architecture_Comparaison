interface UserInput {
  id: number;
  email: string;
  role: string;
  firstName: string;
  lastName: string;
}

export class User {
  private static readonly VALID_ROLES = ['admin', 'reader'];

  private _id: number;
  private _email: string;
  private _role: string;
  private _firstName: string;
  private _lastName: string;

  constructor({ id, email, role, firstName, lastName }: UserInput) {
    this._id = id;
    this._email = email;
    this._role = role;
    this._firstName = firstName;
    this._lastName = lastName;
  }

  static create(input: UserInput): User {
    if (!User.VALID_ROLES.includes(input.role)) {
      throw new Error(`Role '${input.role}' not recognized. Valid roles are: ${User.VALID_ROLES.join(', ')}`);
    }

    return new User(input);
  }

  get id(): number {
    return this._id;
  }

  get email(): string {
    return this._email;
  }

  get role(): string {
    return this._role;
  }

  get firstName(): string {
    return this._firstName;
  }

  get lastName(): string {
    return this._lastName;
  }
}
