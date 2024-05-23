export interface IProjects {
    id: number,
    name: string,
    description: string,
    img: string,
    tags: string[],
    employees_count: number,
    profile_id: number,
    user_id: number,
    category_id: number,
    createdAt: Date,
    launch_date: Date,
    is_active: boolean,
    is_launched: boolean,
    need_investores: boolean,
}