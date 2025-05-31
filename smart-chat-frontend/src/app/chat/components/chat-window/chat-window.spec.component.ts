/// <reference types="jasmine" />
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { beforeEach, describe, it } from 'node:test';
import 'zone.js/testing';
import { ChatWindow } from './chat-window.component';

describe('ChatWindow', () => {
  let component: ChatWindow;
  let fixture: ComponentFixture<ChatWindow>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ChatWindow]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ChatWindow);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

