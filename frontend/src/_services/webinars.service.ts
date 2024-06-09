import type { IPagination, IResponse } from "@/_interfaces/global.interface"
import type { IWebinars } from "@/_interfaces/webinars.interface"
import { prepareSearchPagination } from "@/_libs/requestify.lib"
import { HttpClient } from "@/_interfaces/httpClient"

const http = new HttpClient()
export const _controller = "webinars"
export const create = async (_values: IWebinars) => {
	return http.create<IWebinars>(_controller, _values)
}

export const update = async (_values: IWebinars) => {
	return http.update<IWebinars>(_controller, _values.id, _values)
}

export const findById = async (itemId: IWebinars["id"]) => {
	return http.get<IWebinars>(_controller, itemId)
}

export const find = async (pagination: IPagination): Promise<IResponse<IWebinars[]> | null> => {
	return http.getAll<IWebinars>(prepareSearchPagination(_controller, pagination))
}

export const destroy = async (itemId: IWebinars["id"]) => http.delete(_controller, itemId)
