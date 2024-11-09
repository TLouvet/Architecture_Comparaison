import { IsString, IsEmail, MaxLength, IsOptional } from 'class-validator';

export class UserDTO {
  @IsOptional()
  id?: number;

  @IsEmail()
  email: string;

  @IsString()
  @MaxLength(100)
  firstName: string;

  @IsString()
  @MaxLength(100)
  lastName: string;

  @IsString()
  role: string;
}
