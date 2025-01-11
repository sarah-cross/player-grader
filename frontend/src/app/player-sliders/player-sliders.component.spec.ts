import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlayerSlidersComponent } from './player-sliders.component';

describe('PlayerSlidersComponent', () => {
  let component: PlayerSlidersComponent;
  let fixture: ComponentFixture<PlayerSlidersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PlayerSlidersComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PlayerSlidersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
