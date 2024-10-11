import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {STORAGE_MODULE_DECLARATIONS, StorageRoutingModule} from  './Storage-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    StorageRoutingModule
  ],
  declarations: STORAGE_MODULE_DECLARATIONS,
  exports: STORAGE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class StorageModule { }