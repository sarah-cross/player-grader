import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlayerGradingComponent } from './player-grading.component';

describe('PlayerGradingComponent', () => {
  let component: PlayerGradingComponent;
  let fixture: ComponentFixture<PlayerGradingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PlayerGradingComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PlayerGradingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
