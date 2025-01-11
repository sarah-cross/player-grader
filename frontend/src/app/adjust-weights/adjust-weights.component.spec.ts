import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdjustWeightsComponent } from './adjust-weights.component';

describe('AdjustWeightsComponent', () => {
  let component: AdjustWeightsComponent;
  let fixture: ComponentFixture<AdjustWeightsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AdjustWeightsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AdjustWeightsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
