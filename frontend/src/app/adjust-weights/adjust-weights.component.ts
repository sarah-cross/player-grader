import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-adjust-weights',
  templateUrl: './adjust-weights.component.html',
  styleUrls: ['./adjust-weights.component.css']
})
export class AdjustWeightsComponent implements OnInit {
  attributes = [
    { name: 'Shooting', weight: 1 },
    { name: 'Ball Handling', weight: 1 },
    { name: 'Defense', weight: 1 },
    { name: 'Basketball IQ', weight: 1 },
    { name: 'Athleticism', weight: 1 },
    { name: 'Rebounding', weight: 1 },
    { name: 'Upside', weight: 1 }
  ];

  ngOnInit(): void {
    // Load saved weights from localStorage if available
    const savedWeights = localStorage.getItem('attributeWeights');
    if (savedWeights) {
      this.attributes = JSON.parse(savedWeights);
    }
  }

  saveWeights(): void {
    localStorage.setItem('attributeWeights', JSON.stringify(this.attributes));
    alert('Weights saved successfully!');
  }
}
