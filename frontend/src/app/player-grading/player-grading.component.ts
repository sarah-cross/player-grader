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
    position: 'Guard',
    height: '6\'5"',
    weight: '186 lbs',
    image: 'http://localhost:8000/player_images/caruso.webp',
    stats: {
      pts: 12.3,
      reb: 4.5,
      ast: 3.8,
      stl: 1.2
    }
  };

  grade = 'A';

  attributes = [
    { name: 'Shooting', value: 80, weight: 1 },
    { name: 'Ball Handling', value: 75, weight: 1 },
    { name: 'Defense', value: 90, weight: 1 },
    { name: 'Basketball IQ', value: 85, weight: 1 },
    { name: 'Athleticism', value: 88, weight: 1 },
    { name: 'Rebounding', value: 70, weight: 1 },
    { name: 'Upside', value: 95, weight: 1 }
  ];


  ngOnInit(): void {
    // Load saved weights from localStorage
    const savedWeights = localStorage.getItem('attributeWeights');
    if (savedWeights) {
      const loadedWeights = JSON.parse(savedWeights);
      this.attributes.forEach((attr, index) => {
        attr.weight = loadedWeights[index].weight;
      });
    }

    this.calculateGrade();
  }

  calculateGrade(): void {
    const total = this.attributes.reduce((sum, attr) => sum + attr.value * attr.weight, 0);
    const average = total / this.attributes.length;

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

  // Method to get background color based on grade
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
      case 'D': return '#F57C00';  // Dark Orange
      case 'D-': return '#E65100'; // Red-Orange
      case 'F': return '#F44336';  // Red
      default: return '#000';      // Black for undefined grades
    }
  }
}
