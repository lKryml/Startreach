import { LucidIcon } from './global.interface';
export interface IMenuItem {
    id: string,
    path?: string,
    url?: string,
    icon?: typeof LucidIcon,
    label?: string,
    children?: IMenuItem[];
    isHidden?: boolean
    isDisabled?: boolean,
    isSeparator?: boolean
}

export interface IMenuProps {
    items: IMenuItem[],
}