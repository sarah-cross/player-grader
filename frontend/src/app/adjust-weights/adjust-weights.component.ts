import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-adjust-weights',
  templateUrl: './adjust-weights.component.html',
  styleUrls: ['./adjust-weights.component.css'],
})
export class AdjustWeightsComponent implements OnInit {
  positions: string[] = [
    'Point Guard',
    'Shooting Guard',
    'Small Forward',
    'Power Forward',
    'Center',
    'All Positions',
  ];
  selectedPositions: string[] = [];
  features: string[] = [
    'Shooting',
    'Ball Handling',
    'Defense',
    'Basketball IQ',
    'Athleticism',
    'Rebounding',
    'Upside',
  ];

  importanceOptions = [
    { label: 'Minimally Important', value: 'minimally' },
    { label: 'Fairly Important', value: 'fairly' },
    { label: 'Important', value: 'important' },
    { label: 'Very Important', value: 'very' },
  ];

  // Structure: { position: { feature: weight } }
  weights: { [position: string]: { [feature: string]: string } } = {};

  ngOnInit(): void {
    const savedWeights = localStorage.getItem('featureWeights');
    if (savedWeights) {
      this.weights = JSON.parse(savedWeights);
    }
    
    const savedPositions = localStorage.getItem('selectedPositions');
    if (savedPositions) {
      this.selectedPositions = JSON.parse(savedPositions);
      this.selectedPositions.forEach(position => {
        if (!this.weights[position]) {
          this.weights[position] = {};
        }
        this.features.forEach(feature => {
          if (!this.weights[position][feature]) {
            this.weights[position][feature] = '';
          }
        });
      });
    }
  }
  
  

  onPositionChange(): void {
    this.selectedPositions.forEach(position => {
      if (!this.weights[position]) {
        this.weights[position] = {};
      }
      this.features.forEach(feature => {
        if (!this.weights[position][feature]) {
          this.weights[position][feature] = ''; // Avoid redundant initialization
        }
      });
    });
  }
  
  
  onWeightChange(position: string, feature: string, value: string): void {
    if (this.positions.includes(position)) {
      if (!this.weights[position]) {
        this.weights[position] = {};
      }
      this.weights[position][feature] = value;
      console.log(`Updated weight for ${position}, ${feature}: ${value}`);
    }
  }
  
  
  saveWeights(): void {
    const validWeights = Object.keys(this.weights).reduce((acc, position) => {
      if (this.positions.includes(position)) {
        acc[position] = this.weights[position];
      }
      return acc;
    }, {} as { [position: string]: { [feature: string]: string } });
  
    localStorage.setItem('featureWeights', JSON.stringify(validWeights));
    console.log('Weights saved:', JSON.stringify(validWeights, null, 2));
    alert('Weights saved successfully!');
  }
  
    

  allWeightsSelected(): boolean {
    // Ensure at least one position is selected
    if (this.selectedPositions.length === 0) {
      return false;
    }
  
    // Check if all features for the first selected position have weights assigned
    const position = this.selectedPositions[0];
    return this.features.every(
      feature => this.weights[position]?.[feature] !== undefined && this.weights[position][feature] !== ''
    );
  }
  

  openSettings(): void {
    console.log('Settings button clicked');
  }
}
