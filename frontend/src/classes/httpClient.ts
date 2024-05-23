class HttpClient {
	private baseUrl: string

	constructor(baseUrl: string) {
		this.baseUrl = baseUrl
	}
	private _getHeaders() {
		const token = localStorage.getItem("access_token")
		return {
			"Content-Type": "application/json",
			Authorization: `Bearer ${token}`
		}
	}
	// Generic method for CRUD operations
	private async fetchData<T>(url: string, method: string, data?: any): Promise<T | null> {
		const response = await fetch(`${this.baseUrl}${url}`, {
			method,
			headers: this._getHeaders(),
			body: data ? JSON.stringify(data) : undefined
		})

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`)
		}

		const contentType = response.headers.get("content-type")
		if (contentType && contentType.includes("application/json")) {
			return (await response.json()) as T
		}

		return null
	}

	// Create
	async create<T>(resource: string, data: any): Promise<T | null> {
		return await this.fetchData<T>(resource, "POST", data)
	}

	// Read (all)
	async getAll<T>(resource: string): Promise<T[] | null> {
		return await this.fetchData<T[]>(resource, "GET")
	}

	// Read (single)
	async get<T>(resource: string, id: string): Promise<T | null> {
		return await this.fetchData<T>(`${resource}/${id}`, "GET")
	}

	// Update
	async update<T>(resource: string, id: string, data: any): Promise<T | null> {
		return await this.fetchData<T>(`${resource}/${id}`, "PUT", data)
	}

	// Delete
	async delete(resource: string, id: string): Promise<void> {
		await this.fetchData<void>(`${resource}/${id}`, "DELETE")
	}
}
