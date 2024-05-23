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
	createdAt: Date
    attendees: number
	
}