import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PlayerGradingComponent } from './player-grading/player-grading.component';
import { AdjustWeightsComponent } from './adjust-weights/adjust-weights.component';
import { FindPlayersComponent } from './find-players/find-players.component';

const routes: Routes = [
  { path: 'player-grading', component: PlayerGradingComponent },
  { path: 'find-players', component: FindPlayersComponent },
  { path: 'adjust-weights', component: AdjustWeightsComponent },
  { path: '', redirectTo: '/player-grading', pathMatch: 'full' } // Default route
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
