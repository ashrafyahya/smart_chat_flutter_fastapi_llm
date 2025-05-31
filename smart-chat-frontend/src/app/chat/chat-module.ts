import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ChatRoutingModule } from './chat-routing-module';
import { Chat } from './chat';

import { FormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatListModule } from '@angular/material/list';
import { MatButtonModule } from '@angular/material/button';


@NgModule({
  declarations: [
    Chat
  ],
  imports: [
    CommonModule,
    ChatRoutingModule,
    FormsModule,
    MatCardModule,
    MatInputModule,
    MatListModule,
    MatButtonModule
  ]
})
export class ChatModule { }
