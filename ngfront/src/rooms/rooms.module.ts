import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RoomComponent } from './components/room/room.component';
import { RoomsRoutingModule } from './rooms-routing.module';



@NgModule({
  declarations: [
    RoomComponent
  ],
  imports: [
    CommonModule,
    RoomsRoutingModule
  ]
})
export class RoomsModule { }
