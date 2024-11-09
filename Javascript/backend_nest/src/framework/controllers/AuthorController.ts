import { Controller, Get, Post, Put, Delete, Param, Body, NotFoundException, Inject, HttpCode } from '@nestjs/common';
import { Author } from 'src/domain/entities/Author';
import { Mapper } from 'src/domain/kernel/Mapper';
import { IAuthorService } from 'src/domain/services/IAuthorService';
import { AuthorDTO } from 'src/dto/schema/AuthorDTO';

@Controller('authors')
export class AuthorController {
  constructor(
    @Inject('Service')
    private readonly authorService: IAuthorService,
    @Inject('DTOMapper')
    private readonly authorMapper: Mapper<Author, AuthorDTO>
  ) {}

  @Get()
  async listAuthors() {
    const authors = await this.authorService.listAllAuthors();
    return this.authorMapper.toExternalList(authors);
  }

  @Get(':authorId')
  async getAuthor(@Param('authorId') authorId: number) {
    const author = await this.authorService.getAuthorById(authorId);
    if (!author) {
      throw new NotFoundException('Author not found');
    }

    return this.authorMapper.toExternal(author);
  }

  @Post()
  async createAuthor(@Body() createAuthorDto: AuthorDTO) {
    const author = this.authorMapper.toDomain(createAuthorDto);
    const createdAuthor = await this.authorService.createAuthor(author);
    return this.authorMapper.toExternal(createdAuthor);
  }

  @Put(':authorId')
  async updateAuthor(@Param('authorId') authorId: number, @Body() updateAuthorDto: AuthorDTO) {
    const updatedAuthor = this.authorMapper.toDomain(updateAuthorDto);
    const result = await this.authorService.updateAuthor(authorId, updatedAuthor);
    if (!result) {
      throw new NotFoundException('Author not found');
    }
    return this.authorMapper.toExternal(result);
  }

  @Delete(':authorId')
  @HttpCode(204)
  deleteAuthor(@Param('authorId') authorId: number) {
    this.authorService.deleteAuthor(authorId);
    return {};
  }
}
