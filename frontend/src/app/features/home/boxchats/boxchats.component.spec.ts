import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BoxchatsComponent } from './boxchats.component';

describe('BoxchatsComponent', () => {
  let component: BoxchatsComponent;
  let fixture: ComponentFixture<BoxchatsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BoxchatsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BoxchatsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
