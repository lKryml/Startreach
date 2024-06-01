export interface IPosts {
    id: number,
    title: string,
    post: string,
    img: string,
    img64: string,
    tags: string[],
    profile_id: number,
    user_id: number,
    category_id: number,
    createdAt: Date,
    is_active: boolean,
}