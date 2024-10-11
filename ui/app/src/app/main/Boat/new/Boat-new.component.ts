import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Boat-new',
  templateUrl: './Boat-new.component.html',
  styleUrls: ['./Boat-new.component.scss']
})
export class BoatNewComponent {
  @ViewChild("BoatForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}