import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'admin',
    loadChildren: () => import('../admin/admin.module').then(m => m.AdminModule)
  },
  {
    path: 'accounts',
    loadChildren: () => import('../accounts/accounts.module').then(m => m.AccountsModule)
  },
  {
    path: 'rooms',
    loadChildren: () => import('../rooms/rooms.module').then(m => m.RoomsModule)
  },
  {
    path: 'rooms/:roomId',
    loadChildren: () => import('../room-details/room-details.module').then(m => m.RoomDetailsModule)
  },
  { 
    path: '', 
    redirectTo: 'rooms', 
    pathMatch: 'full' 
  } 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }