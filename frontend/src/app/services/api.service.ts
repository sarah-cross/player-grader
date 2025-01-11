

// SERVICES FETCH OR SEND DATA BETWEEN FRONTEND AND BACKEND

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private baseUrl = 'http://localhost:8000/api'; // Base URL for your Django API

  constructor(private http: HttpClient) {}

  // Fetch all players
  getPlayers(): Observable<any> {
    return this.http.get(`${this.baseUrl}/players/`);
  }

  // Add a new player
  addPlayer(player: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/players/`, player);
  }

  // Fetch a single player by ID
  getPlayerById(playerId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/players/${playerId}/`);
  }

  // Update an existing player
  updatePlayer(playerId: number, player: any): Observable<any> {
    return this.http.put(`${this.baseUrl}/players/${playerId}/`, player);
  }

  // Delete a player
  deletePlayer(playerId: number): Observable<any> {
    return this.http.delete(`${this.baseUrl}/players/${playerId}/`);
  }
}

