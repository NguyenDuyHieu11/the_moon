// websocket.service.ts
// import { WebSocket } from 'ws';
import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';

// WebSocket = require('ws');
@Injectable({
  providedIn: 'root',
})
export class WebSocketService {
  private socket$: WebSocketSubject<any>;
  roomName!: string; /*HAVE NOT DEALED WITH THIS YET*/

  constructor() {
    this.socket$ = webSocket({
      // use wss for https support
      url: this.createWebSocketUrl()
    });
  }

  private createWebSocketUrl(): string {
    return `ws://127.0.0.1:8000/ws/chat/${this.roomName}/`;
  }

  sendMessage(message: string): void {
    this.socket$.next({ message });
  }

  getMessage() {
    return this.socket$.asObservable();
  }
}