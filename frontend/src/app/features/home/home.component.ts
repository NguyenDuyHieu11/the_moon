import { Component } from '@angular/core';
import { ChatComponent } from "./mainchat/chat.component";
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [ChatComponent, RouterModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

    messageOnSent(message: string) {

    }
}
