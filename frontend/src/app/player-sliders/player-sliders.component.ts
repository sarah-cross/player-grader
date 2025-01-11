import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-player-sliders',
  templateUrl: './player-sliders.component.html',
  styleUrls: ['./player-sliders.component.css']
})
export class PlayerSlidersComponent {
  @Input() attributes: any[] = []; // Array of attributes passed from parent
  @Output() slidersUpdated = new EventEmitter<void>(); // Notify parent of updates

  onSliderChange(event: any, attribute: any): void {
    attribute.value = event.value; // Update the slider's value
    this.slidersUpdated.emit(); // Emit event to notify parent
  }
}

