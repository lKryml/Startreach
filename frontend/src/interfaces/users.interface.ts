import type { UsersTypes } from "@/constants/usersTypes.contant";

export interface IUsers {
    first_name: string;
    last_name: string;
    email: string;
    password: string;
    profile_id: string;
    access_token: string;
    refresh_token: string;
    user_type: UsersTypes
}