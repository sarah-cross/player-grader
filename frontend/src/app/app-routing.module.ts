import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PlayerGradingComponent } from './player-grading/player-grading.component';
import { AdjustWeightsComponent } from './adjust-weights/adjust-weights.component';

const routes: Routes = [
  { path: 'player-grading', component: PlayerGradingComponent },
  { path: 'adjust-weights', component: AdjustWeightsComponent },
  { path: '', redirectTo: '/player-grading', pathMatch: 'full' } // Default route
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
