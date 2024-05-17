import { HomeIcon } from 'lucide-vue-next';

export interface IMenuItem {
    id: string,
    path?: string,
    url?: string,
    icon?: typeof HomeIcon,
    label?: string,
    children?: IMenuItem[];
    isHidden?: boolean
    isDisabled?: boolean,
    isSeparator?: boolean
}

export interface IMenuProps {
    items: IMenuItem[],
}