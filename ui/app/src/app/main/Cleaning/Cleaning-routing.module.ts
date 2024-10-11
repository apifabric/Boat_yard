import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CleaningHomeComponent } from './home/Cleaning-home.component';
import { CleaningNewComponent } from './new/Cleaning-new.component';
import { CleaningDetailComponent } from './detail/Cleaning-detail.component';

const routes: Routes = [
  {path: '', component: CleaningHomeComponent},
  { path: 'new', component: CleaningNewComponent },
  { path: ':id', component: CleaningDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Cleaning-detail-permissions'
      }
    }
  }
];

export const CLEANING_MODULE_DECLARATIONS = [
    CleaningHomeComponent,
    CleaningNewComponent,
    CleaningDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CleaningRoutingModule { }