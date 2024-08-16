import { Component } from '@angular/core';
import { Subscription } from 'rxjs';
import { WebSocketService } from '../../services/websocket.service';

@Component({
    selector: 'app-chat',
    standalone: true,
    templateUrl: './chat.component.html',
    styleUrl: './chat.component.css'
})
export class ChatComponent {
    private subscription!: Subscription;

    constructor(
        private webSocketService: WebSocketService,
    ) { }

    sendMessage(message: string): void {
        this.webSocketService.sendMessage(message)

        this.subscription = this.webSocketService.getMessage().subscribe({
            next: (res: any) => {
                console.log(res);
            },
        });
    }
}