import type { IPagination } from "@/interfaces/global.interface";

export const prepareSearchPagination = (path: string, pagination: IPagination): string => {
    let URL = `${path}?page=${pagination.page || 1}&per_page=${pagination.per_page || 20}`;
    URL += pagination.sort ? `&sort=${pagination.sort}` : '';
    URL += pagination.sortBy ? `&sort=${pagination.sortBy}` : '';
    return URL;
}