import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Boat-card.component.html',
  styleUrls: ['./Boat-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Boat-card]': 'true'
  }
})

export class BoatCardComponent {


}