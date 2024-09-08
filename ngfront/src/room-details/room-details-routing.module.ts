import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RoomDetailsComponent } from './components/room-details/room-details.component';
import { RoomMemberListComponent } from './components/room-member-list/room-member-list.component';
import { TodoListComponent } from './components/todo-list/todo-list.component';

const routes: Routes = [
  {
    path: 'room-details', 
    component: RoomDetailsComponent
  },
  {
    path: 'room-members', 
    component: RoomMemberListComponent
  },
  {
    path: 'room-todos', 
    component: TodoListComponent
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class RoomDetailsRoutingModule { }