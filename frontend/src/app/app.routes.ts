import { Routes } from '@angular/router';
import path from 'path';
import { ChatComponent } from './features/home/mainchat/chat.component';
import { HomeComponent } from './features/home/home.component';

export const routes: Routes = [
    { path: "chat", component: ChatComponent },
    { path: "home", component: HomeComponent },
];
