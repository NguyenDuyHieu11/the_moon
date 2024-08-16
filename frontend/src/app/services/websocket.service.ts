// websocket.service.ts
// import { WebSocket } from 'ws';
import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';

global.WebSocket = require('ws');
@Injectable({
  providedIn: 'root',
})
export class WebSocketService {
  private socket$: WebSocketSubject<any>;
  
  constructor() {
    this.socket$ = webSocket({
      // use wss for https support
      url: 'ws://localhost:8000/ws/chat/',
    });
  }

  sendMessage(message: string): void {
    this.socket$.next({ message });
  }

  getMessage() {
    return this.socket$.asObservable();
  }
}