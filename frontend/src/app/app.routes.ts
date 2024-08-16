import { Routes } from '@angular/router';
import path from 'path';
import { ChatComponent } from './features/chat/chat.component';
import { HomeComponent } from './features/home/home.component';

export const routes: Routes = [
    { path: "chat", component: ChatComponent, outlet: "primary" },
    { path: "home", component: HomeComponent, outlet: "secondary" },
];
