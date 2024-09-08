import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RoomListComponent } from './components/room-list/room-list.component';
import { RoomCreateComponent } from './components/room-create/room-create.component';
import { RoomEditComponent } from './components/room-edit/room-edit.component';
import { RoomDeleteComponent } from './components/room-delete/room-delete.component';
import { AdminRoutingModule } from './admin-routing.module';



@NgModule({
  declarations: [
    RoomListComponent,
    RoomCreateComponent,
    RoomEditComponent,
    RoomDeleteComponent
  ],
  imports: [
    CommonModule,
    AdminRoutingModule
  ]
})
export class AdminModule { }
