import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Cleaning-card.component.html',
  styleUrls: ['./Cleaning-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Cleaning-card]': 'true'
  }
})

export class CleaningCardComponent {


}