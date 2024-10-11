import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {CLEANING_MODULE_DECLARATIONS, CleaningRoutingModule} from  './Cleaning-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CleaningRoutingModule
  ],
  declarations: CLEANING_MODULE_DECLARATIONS,
  exports: CLEANING_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CleaningModule { }