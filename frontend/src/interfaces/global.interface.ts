export { FileIcon as LucidIcon } from "lucide-vue-next";

export interface IDetailsProps<T> {
    defaultItemId?: string;
    defaultItem?: T
}

export interface ILocation {
    lang: number;
    lat: number;
}
export interface IPagination {
    page: number;
    per_page: number;
    total?: number;
    totalPages?: number;
    sort?: 'asc' | 'desc';
    sortBy?: string;
    search?: string;
    queries?: string;
}

export interface IResponse<T> {
    data: T,
    status: string,
    statusCode: number,
    count: number,
}

