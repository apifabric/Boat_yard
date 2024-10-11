import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StorageHomeComponent } from './home/Storage-home.component';
import { StorageNewComponent } from './new/Storage-new.component';
import { StorageDetailComponent } from './detail/Storage-detail.component';

const routes: Routes = [
  {path: '', component: StorageHomeComponent},
  { path: 'new', component: StorageNewComponent },
  { path: ':id', component: StorageDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Storage-detail-permissions'
      }
    }
  }
];

export const STORAGE_MODULE_DECLARATIONS = [
    StorageHomeComponent,
    StorageNewComponent,
    StorageDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class StorageRoutingModule { }