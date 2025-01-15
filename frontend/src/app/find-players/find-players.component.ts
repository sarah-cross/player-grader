import { Component, OnInit } from '@angular/core';
import { PlayerService } from '../services/player.service'; 
import { PageEvent } from '@angular/material/paginator';

interface Player {
  name: string;
  position: string;
  height: string;
  weight: number;
  headshot: string | null; // headshot could be null if not set
}

@Component({
  selector: 'app-find-players',
  templateUrl: './find-players.component.html',
  styleUrls: ['./find-players.component.css']
})


export class FindPlayersComponent implements OnInit {
  players: Player[] = [];
  filteredPlayers: Player[] = [];
  paginatedPlayers: Player[] = []; // Players to display on the current page

  positionMapping: { [key: string]: string } = {
    'Point Guard': 'PG',
    'Shooting Guard': 'SG',
    'Small Forward': 'SF',
    'Power Forward': 'PF',
    'Center': 'C',
  };
  
  positions = Object.keys(this.positionMapping);
  selectedPositions: string[] = [];

  pageSize = 12; // Number of players per page
  currentPage = 0; // Current page index
  
  constructor(private playerService: PlayerService) {}


  ngOnInit() {
    this.playerService.getPlayers().subscribe(players => {
      this.players = players.sort((a: { name: string; }, b: { name: any; }) => a.name.localeCompare(b.name));
      this.filteredPlayers = [...this.players];
      this.updatePaginatedPlayers();
    });
  }

  togglePosition(position: string) {
    if (this.selectedPositions.includes(position)) {
      this.selectedPositions = this.selectedPositions.filter(pos => pos !== position); // Remove position
    } else {
      this.selectedPositions.push(position); // Add position
    }

    this.applyFilters();
  }

  applyFilters() {
    if (this.selectedPositions.length > 0) {
      const selectedAbbreviations = this.selectedPositions.map(
        pos => this.positionMapping[pos] 
      );
  
      this.filteredPlayers = this.players.filter(player =>
        selectedAbbreviations.includes(player.position)
      );
    } else {
      this.filteredPlayers = [...this.players]; // Reset to all players
    }
  
    this.currentPage = 0; // Reset to first page after filtering
    this.updatePaginatedPlayers();
  }
  

  onPlayerSelect(player: any) {
    // Redirect to grading page for the player
    console.log(`Selected player: ${player.name}`);
  } 

  onSearch(event: any) {
    const query = event.target.value.toLowerCase();
    this.filteredPlayers = this.players.filter(player =>
      player.name.toLowerCase().includes(query)
    );
    this.currentPage = 0; // Reset to first page after filtering
    this.updatePaginatedPlayers();
  }

  onPageChange(event: PageEvent) {
    this.pageSize = event.pageSize;
    this.currentPage = event.pageIndex;
    this.updatePaginatedPlayers();
  }

  private updatePaginatedPlayers() {
    const startIndex = this.currentPage * this.pageSize;
    const endIndex = startIndex + this.pageSize;
    this.paginatedPlayers = this.filteredPlayers.slice(startIndex, endIndex);
  }


}
