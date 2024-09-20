import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Subscription } from 'rxjs';
import { WebSocketService } from '../../../services/websocket.service';
import { FormsModule } from '@angular/forms';  

@Component({
    selector: 'app-chat',
    standalone: true,
    templateUrl: './chat.component.html',
    styleUrl: './chat.component.css',
    imports: [FormsModule]
})
export class ChatComponent implements OnInit {
    // private subscription!: Subscription;
    message: string = ''
    @Output() messagePayload = new EventEmitter<string>();

    constructor(
        private webSocketService: WebSocketService,
    ) { }

    // sendMessage(message: string): void {
    //     this.webSocketService.sendMessage(message)

    //     this.subscription = this.webSocketService.getMessage().subscribe({
    //         next: (res: any) => {
    //             console.log(res);
    //         },
    //     });
    // }
    sendMessage(): void{
        if(this.message === '')  {
            this.messagePayload.emit(this.message)
        }
    }

    ngOnInit(): void {
        
    }
}