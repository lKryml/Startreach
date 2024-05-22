export { FileIcon as LucidIcon } from "lucide-vue-next";

export interface IDetailsProps<T> {
    itemId?: string;
    defaultItem?: T
}

export interface IPagination {
    page: number;
    per_page: number;
    sort?: 'asc' | 'desc';
    sortBy?: string;
    search?: string;
    queries?: string;
}

