import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Appointment', loadChildren: () => import('./Appointment/Appointment.module').then(m => m.AppointmentModule) },
    
        { path: 'Billing', loadChildren: () => import('./Billing/Billing.module').then(m => m.BillingModule) },
    
        { path: 'Boat', loadChildren: () => import('./Boat/Boat.module').then(m => m.BoatModule) },
    
        { path: 'Cleaning', loadChildren: () => import('./Cleaning/Cleaning.module').then(m => m.CleaningModule) },
    
        { path: 'Customer', loadChildren: () => import('./Customer/Customer.module').then(m => m.CustomerModule) },
    
        { path: 'Employee', loadChildren: () => import('./Employee/Employee.module').then(m => m.EmployeeModule) },
    
        { path: 'Maintenance', loadChildren: () => import('./Maintenance/Maintenance.module').then(m => m.MaintenanceModule) },
    
        { path: 'Order', loadChildren: () => import('./Order/Order.module').then(m => m.OrderModule) },
    
        { path: 'Part', loadChildren: () => import('./Part/Part.module').then(m => m.PartModule) },
    
        { path: 'Repair', loadChildren: () => import('./Repair/Repair.module').then(m => m.RepairModule) },
    
        { path: 'Service', loadChildren: () => import('./Service/Service.module').then(m => m.ServiceModule) },
    
        { path: 'Storage', loadChildren: () => import('./Storage/Storage.module').then(m => m.StorageModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }