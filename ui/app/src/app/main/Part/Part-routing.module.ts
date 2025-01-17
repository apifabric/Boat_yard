import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PartHomeComponent } from './home/Part-home.component';
import { PartNewComponent } from './new/Part-new.component';
import { PartDetailComponent } from './detail/Part-detail.component';

const routes: Routes = [
  {path: '', component: PartHomeComponent},
  { path: 'new', component: PartNewComponent },
  { path: ':id', component: PartDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Part-detail-permissions'
      }
    }
  },{
    path: ':part_id/Order', loadChildren: () => import('../Order/Order.module').then(m => m.OrderModule),
    data: {
        oPermission: {
            permissionId: 'Order-detail-permissions'
        }
    }
}
];

export const PART_MODULE_DECLARATIONS = [
    PartHomeComponent,
    PartNewComponent,
    PartDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PartRoutingModule { }