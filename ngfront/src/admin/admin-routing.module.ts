import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RoomCreateComponent } from './components/room-create/room-create.component';
import { RoomEditComponent } from './components/room-edit/room-edit.component';
import { RoomDeleteComponent } from './components/room-delete/room-delete.component';
import { RoomListComponent } from './components/room-list/room-list.component';
const routes: Routes = [
    {
        path: 'room-create', 
        component: RoomCreateComponent
    },
    {
        path: 'room-list', 
        component: RoomListComponent
    },
    {
        path: 'room-edit', 
        component: RoomEditComponent
    },
    {
        path: 'room-delete', 
        component: RoomDeleteComponent
    }
    
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AdminRoutingModule { }