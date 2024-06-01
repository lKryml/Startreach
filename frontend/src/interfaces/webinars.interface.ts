import type { ILocation } from "./global.interface"

export interface IWebinars {
	id: number
	name: string
	description: string
	img: string
	tags: string[]
	guests: string[]
	profile_id: number
	user_id: number
	category_id: number
	attendees: number
	start_date: Date
	end_date: Date
	createdAt: Date
	location: ILocation
}