import { type ILocation } from './global.interface'
import type { UsersTypes } from "@/constants/usersTypes.contant"

export interface IProfile {
    id: number,
    phones: string[], // [09283232323, 094334234234432423234]
    name: string,
    email: string,
    avatar: string,
    bio: string,
    address: string,
    type: UsersTypes,
    user_id: number,
    created_at: string,
    info: IProfileInfo
}

export interface IProfileInfo {
    since: Date,
    location: ILocation,
    img: string, // for profile background
    profile_id: IProfile['id'],
    employees_count: number,
}