import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class PlayerService {
  private apiUrl = 'http://127.0.0.1:8000/api/players/'; // Update with your API endpoint

  constructor(private http: HttpClient) {}

  getPlayers(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }
}
