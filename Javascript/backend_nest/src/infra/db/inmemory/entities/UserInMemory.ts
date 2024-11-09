export class UserInMemory {
  id: number;
  email: string;
  role: string;
  firstName: string;
  lastName: string;

  constructor(id: number, email: string, role: string, firstName: string, lastName: string) {
    this.id = id;
    this.email = email;
    this.role = role;
    this.firstName = firstName;
    this.lastName = lastName;
  }
}
