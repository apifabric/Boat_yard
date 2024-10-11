import { MenuRootItem } from 'ontimize-web-ngx';

import { AppointmentCardComponent } from './Appointment-card/Appointment-card.component';

import { BillingCardComponent } from './Billing-card/Billing-card.component';

import { BoatCardComponent } from './Boat-card/Boat-card.component';

import { CleaningCardComponent } from './Cleaning-card/Cleaning-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { MaintenanceCardComponent } from './Maintenance-card/Maintenance-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { PartCardComponent } from './Part-card/Part-card.component';

import { RepairCardComponent } from './Repair-card/Repair-card.component';

import { ServiceCardComponent } from './Service-card/Service-card.component';

import { StorageCardComponent } from './Storage-card/Storage-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Appointment', name: 'APPOINTMENT', icon: 'view_list', route: '/main/Appointment' }
    
        ,{ id: 'Billing', name: 'BILLING', icon: 'view_list', route: '/main/Billing' }
    
        ,{ id: 'Boat', name: 'BOAT', icon: 'view_list', route: '/main/Boat' }
    
        ,{ id: 'Cleaning', name: 'CLEANING', icon: 'view_list', route: '/main/Cleaning' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'Maintenance', name: 'MAINTENANCE', icon: 'view_list', route: '/main/Maintenance' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'Part', name: 'PART', icon: 'view_list', route: '/main/Part' }
    
        ,{ id: 'Repair', name: 'REPAIR', icon: 'view_list', route: '/main/Repair' }
    
        ,{ id: 'Service', name: 'SERVICE', icon: 'view_list', route: '/main/Service' }
    
        ,{ id: 'Storage', name: 'STORAGE', icon: 'view_list', route: '/main/Storage' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AppointmentCardComponent

    ,BillingCardComponent

    ,BoatCardComponent

    ,CleaningCardComponent

    ,CustomerCardComponent

    ,EmployeeCardComponent

    ,MaintenanceCardComponent

    ,OrderCardComponent

    ,PartCardComponent

    ,RepairCardComponent

    ,ServiceCardComponent

    ,StorageCardComponent

];