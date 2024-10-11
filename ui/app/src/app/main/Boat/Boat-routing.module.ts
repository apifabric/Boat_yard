import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BoatHomeComponent } from './home/Boat-home.component';
import { BoatNewComponent } from './new/Boat-new.component';
import { BoatDetailComponent } from './detail/Boat-detail.component';

const routes: Routes = [
  {path: '', component: BoatHomeComponent},
  { path: 'new', component: BoatNewComponent },
  { path: ':id', component: BoatDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Boat-detail-permissions'
      }
    }
  },{
    path: ':boat_id/Appointment', loadChildren: () => import('../Appointment/Appointment.module').then(m => m.AppointmentModule),
    data: {
        oPermission: {
            permissionId: 'Appointment-detail-permissions'
        }
    }
},{
    path: ':boat_id/Cleaning', loadChildren: () => import('../Cleaning/Cleaning.module').then(m => m.CleaningModule),
    data: {
        oPermission: {
            permissionId: 'Cleaning-detail-permissions'
        }
    }
},{
    path: ':boat_id/Maintenance', loadChildren: () => import('../Maintenance/Maintenance.module').then(m => m.MaintenanceModule),
    data: {
        oPermission: {
            permissionId: 'Maintenance-detail-permissions'
        }
    }
},{
    path: ':boat_id/Repair', loadChildren: () => import('../Repair/Repair.module').then(m => m.RepairModule),
    data: {
        oPermission: {
            permissionId: 'Repair-detail-permissions'
        }
    }
},{
    path: ':boat_id/Storage', loadChildren: () => import('../Storage/Storage.module').then(m => m.StorageModule),
    data: {
        oPermission: {
            permissionId: 'Storage-detail-permissions'
        }
    }
}
];

export const BOAT_MODULE_DECLARATIONS = [
    BoatHomeComponent,
    BoatNewComponent,
    BoatDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BoatRoutingModule { }