import { IsString, IsOptional, IsArray, MaxLength, IsDateString } from 'class-validator';

export class AuthorDTO {
  @IsOptional()
  id?: number;

  @IsString()
  @MaxLength(100)
  firstName: string;

  @IsString()
  @MaxLength(100)
  lastName: string;

  @IsDateString()
  birthDate: string;

  @IsOptional()
  @IsDateString()
  deathDate?: string;

  @IsString()
  @MaxLength(100)
  nationality: string;

  @IsOptional()
  @IsString()
  @MaxLength(2000)
  biography?: string;

  @IsOptional()
  @IsArray()
  books?: number[];
}
