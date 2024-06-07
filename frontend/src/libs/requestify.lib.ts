import type { IPagination } from "@/interfaces/global.interface";

export const prepareSearchPagination = (path: string, pagination: IPagination): string => {
    let URL = `${path}?page=${pagination.page || 1}&per_page=${pagination.per_page || 20}`;
    console.log(URL)
    URL += pagination.sort ? `&sort=${pagination.sort}` : '';
    console.log(URL)
    URL += pagination.sortBy ? `&sort=${pagination.sortBy}` : '';
    console.log(URL)
    return URL;
}