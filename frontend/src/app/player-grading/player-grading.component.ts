import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-player-grading',
  templateUrl: './player-grading.component.html',
  styleUrls: ['./player-grading.component.css']
})
export class PlayerGradingComponent implements OnInit {
  title = 'Player Grader';

  player = {
    name: 'Alex Caruso',
    position: 'Point Guard',
    height: '6\'5"',
    weight: '186 lbs',
    image: 'http://localhost:8000/player_images/caruso.webp',
    stats: {
      pts: 12.3,
      ast: 3.8,
      reb: 4.5,
      blk: 1.0,
      stl: 1.2,
      tpm: 2.0,
      fgp: 70,
      threepp: 60,
      ftp: 90
    }
  };

  grade = 'A';

  attributes = [
    { name: 'Shooting', value: 80, weight: 'fairly' },
    { name: 'Ball Handling', value: 75, weight: 'fairly' },
    { name: 'Defense', value: 90, weight: 'fairly' },
    { name: 'Basketball IQ', value: 85, weight: 'fairly' },
    { name: 'Athleticism', value: 88, weight: 'fairly' },
    { name: 'Rebounding', value: 70, weight: 'fairly' },
    { name: 'Upside', value: 95, weight: 'fairly' }
  ];
  

  ngOnInit(): void {
    const savedWeights = localStorage.getItem('featureWeights');
    if (savedWeights) {
      const loadedWeights = JSON.parse(savedWeights);
      console.log('Parsed saved weights:', loadedWeights);
  
      // Retrieve weights for the player's position
      const positionWeights = loadedWeights[this.player.position];
      console.log('Weights for position:', this.player.position, positionWeights);
  
      if (positionWeights) {
        this.attributes.forEach(attr => {
          const weight = positionWeights[attr.name];
          attr.weight = weight || 'minimally'; // Default to 'minimally' if no weight is found
        });
      } else {
        console.warn(`No saved weights found for position: ${this.player.position}`);
      }
    } else {
      console.warn('No saved weights found in localStorage.');
    }
  
    this.calculateGrade();
  }
  
  
  

  calculateGrade(): void {
    const weightValues: { [key: string]: number } = {
      minimally: 1,
      fairly: 2,
      important: 3,
      very: 4,
    };
  
    const totalWeight = this.attributes.reduce((sum, attr) => {
      const numericWeight = weightValues[attr.weight] || 1; // Default to 1 for missing weights
      return sum + numericWeight;
    }, 0);
  
    const total = this.attributes.reduce((sum, attr) => {
      const numericWeight = weightValues[attr.weight] || 1;
      return sum + attr.value * numericWeight;
    }, 0);
  
    const average = totalWeight > 0 ? total / totalWeight : 0;
  
    // Update grade based on average
    if (average >= 95) this.grade = 'A+';
    else if (average >= 90) this.grade = 'A';
    else if (average >= 85) this.grade = 'A-';
    else if (average >= 80) this.grade = 'B+';
    else if (average >= 75) this.grade = 'B';
    else if (average >= 70) this.grade = 'B-';
    else if (average >= 65) this.grade = 'C+';
    else if (average >= 60) this.grade = 'C';
    else if (average >= 55) this.grade = 'C-';
    else if (average >= 50) this.grade = 'D+';
    else if (average >= 45) this.grade = 'D';
    else if (average >= 40) this.grade = 'D-';
    else this.grade = 'F';
  }
  
  

  onAttributeChange(attribute: any): void {
    this.calculateGrade();
  }

  getGradeColor(): string {
    switch (this.grade) {
      case 'A+': return '#388E3C'; // Dark Green
      case 'A': return '#4CAF50';  // Green
      case 'A-': return '#66BB6A'; // Light Green
      case 'B+': return '#9CCC65'; // Lime Green
      case 'B': return '#CDDC39';  // Lime
      case 'B-': return '#D4E157'; // Yellow Lime
      case 'C+': return '#FFEB3B'; // Yellow
      case 'C': return '#FFC107';  // Yellow-Orange
      case 'C-': return '#FFA726'; // Orange Yellow
      case 'D+': return '#FB8C00'; // Orange
      case 'D': return '#F57C00'; // Dark Orange
      case 'D-': return '#E65100'; // Red-Orange
      case 'F': return '#F44336';  // Red
      default: return '#000';      // Black for undefined grades
    }
  }
}
