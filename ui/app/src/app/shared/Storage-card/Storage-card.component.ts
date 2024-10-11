import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Storage-card.component.html',
  styleUrls: ['./Storage-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Storage-card]': 'true'
  }
})

export class StorageCardComponent {


}