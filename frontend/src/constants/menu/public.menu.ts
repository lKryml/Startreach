import { type IMenuItem } from "@/interfaces/menu.interface";
import * as Icons from 'lucide-vue-next';
export const menu = <IMenuItem[]>[
    {
        id: 'home',
        path: '/',
        label: 'MENU.HOME',
        icon: Icons.Home,
    }, {
        id: 'about',
        path: '/about',
        label: 'MENU.ABOUT',
        icon: Icons.FilesIcon,
    }, {
        id: 'dashboard',
        path: '/dashboard',
        label: 'MENU.DASHBOARD',
        icon: Icons.PieChartIcon,
    }
];