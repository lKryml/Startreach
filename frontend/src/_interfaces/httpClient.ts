import { enviroment } from "@/enviroments/enviroment"
import type { IPagination, IResponse } from "@/_interfaces"

export class HttpClient {
	private baseUrl: string
	constructor() {
		this.baseUrl = enviroment.apiUrl
		console.log(this.baseUrl)
	}
	private _getHeaders() {
		const token = localStorage.getItem("access_token")
		return {
			"Content-Type": "application/json",
			Authorization: `Bearer ${token}`
		}
	}
	// Generic method for CRUD operations
	private async fetchData<T>(
		url: string,
		method: string,
		data?: any
	): Promise<IResponse<T> | null> {
		const response = await fetch(`${this.baseUrl}/${url}`, {
			method,
			headers: this._getHeaders(),
			body: data && !(data instanceof FormData) ? JSON.stringify(data) : data
		})

		if (!response.ok) {
			if (response.status === 401) {
				location.href = `/auth/login`
			}
			throw new Error(`HTTP error! status: ${response.status}`)
		}

		const contentType = response.headers.get("content-type")
		if (contentType && contentType.includes("application/json")) {
			return (await response.json()) as IResponse<T>
		}

		return null
	}

	// Create
	async create<T>(resource: string, data: any): Promise<IResponse<T> | null> {
		return (await this.fetchData<IResponse<T>>(resource, "POST", data)) as IResponse<T>
	}

	// Read (all)
	async getAll<T>(resource: string, params?: any): Promise<IResponse<T[]> | null> {
		return (await this.fetchData<T[]>(
			`${resource}${resource.includes("?") ? "&" : "?"}${this.getQueryParams(params)}`,
			"GET"
		)) as IResponse<T[]>
	}

	// Read (single)
	async get<T>(resource: string, id: number | string): Promise<IResponse<T> | null> {
		return (await this.fetchData<IResponse<T>>(`${resource}/${id}`, "GET")) as IResponse<T>
	}

	// Update
	async update<T>(
		resource: string,
		id: number | string,
		data: any
	): Promise<IResponse<T> | null> {
		return (await this.fetchData<IResponse<T>>(
			`${resource}/${id}`,
			"PUT",
			data
		)) as IResponse<T>
	}

	// Delete
	async delete(resource: string, id: number | string): Promise<IResponse<any>> {
		return (await this.fetchData<void>(`${resource}/${id}`, "DELETE")) as IResponse<any>
	}

	public getQueryParams(params: IPagination): string {
		if (params) {
			return Object.keys(params)
				.map((key) => `${key}=${(<any>params)[key]}`)
				.join("&")
		} else return ""
	}
}
