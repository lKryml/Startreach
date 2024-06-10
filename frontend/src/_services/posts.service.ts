import type { IPagination, IResponse } from "@/_interfaces/global.interface"
import type { IPosts } from "@/_interfaces/posts.interface"
import { prepareSearchPagination } from "@/_libs/requestify.lib"
import { HttpClient } from "@/_interfaces/httpClient"

const http = new HttpClient()
export const _controller = "posts"
export const create = async (_values: IPosts) => {
	return http.create<IPosts>(_controller, _values)
}

export const update = async (_values: IPosts) => {
	return http.update<IPosts>(_controller, _values.id, _values)
}

export const findById = async (itemId: IPosts["id"]) => {
	return http.get<IPosts>(_controller, itemId)
}

export const find = async (pagination: IPagination): Promise<IResponse<IPosts[]> | null> => {
	return http.getAll<IPosts>(prepareSearchPagination(_controller, pagination))
}

export const destroy = async (itemId: IPosts["id"]) => http.delete(_controller, itemId)
