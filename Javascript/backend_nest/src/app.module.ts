import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { UserModule } from './framework/modules/UserModule';
import { AuthorModule } from './framework/modules/AuthorModule';

@Module({
  imports: [UserModule, AuthorModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
