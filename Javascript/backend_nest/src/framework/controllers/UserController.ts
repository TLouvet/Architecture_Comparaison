import { Controller, Get, Put, Delete, Param, Body, NotFoundException, HttpCode, Inject } from '@nestjs/common';
import { User } from 'src/domain/entities/User';
import { Mapper } from 'src/domain/kernel/Mapper';
import { IUserService } from 'src/domain/services/UserService';
import { UserDTO } from 'src/dto/schema/UserDTO';

@Controller('users')
export class UserController {
  constructor(
    @Inject('Service')
    private readonly userService: IUserService,
    @Inject('DTOMapper')
    private readonly userMapper: Mapper<User, UserDTO>
  ) {}

  @Get()
  async findMany() {
    const users = await this.userService.listAllUsers();
    return this.userMapper.toExternalList(users);
  }

  @Get(':userId')
  async findOne(@Param('userId') userId: number) {
    const user = await this.userService.getUserById(userId);
    if (!user) {
      throw new NotFoundException('Utilisateur non trouvé');
    }
    return this.userMapper.toExternal(user);
  }

  @Put(':userId')
  async updateOne(@Param('userId') userId: number, @Body() updateUserDto: UserDTO) {
    const updatedUser = this.userMapper.toDomain(updateUserDto);
    const result = await this.userService.updateUser(userId, updatedUser);
    if (!result) {
      throw new NotFoundException('Utilisateur non trouvé');
    }
    return this.userMapper.toExternal(result);
  }

  @Delete(':userId')
  @HttpCode(204)
  async delete(@Param('userId') userID: number) {
    this.userService.deleteUser(userID);
    return {};
  }
}
