import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RoomDetailsComponent } from './components/room-details/room-details.component';
import { RoomMemberListComponent } from './components/room-member-list/room-member-list.component';
import { TodoListComponent } from './components/todo-list/todo-list.component';
import { RoomDetailsRoutingModule } from './room-details-routing.module';



@NgModule({
  declarations: [
    RoomDetailsComponent,
    RoomMemberListComponent,
    TodoListComponent
  ],
  imports: [
    CommonModule,
    RoomDetailsRoutingModule
  ]
})
export class RoomDetailsModule { }
