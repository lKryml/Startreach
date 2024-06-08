import { type IPagination } from "@/_interfaces"
interface usePaginationProps {
	pagination: IPagination
}
export const usePagination = (route: any): usePaginationProps => {
	const pagination = <IPagination>{
		page: route.query.page || 1,
		per_page: route.query.per_page || 20,
		sort: route.query.sort,
		sortBy: route.query.sortBy,
		search: route.query.search,
		queries: route.query.queries
	}
	return { pagination }
}
