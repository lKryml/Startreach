import type { UsersTypes } from "@/constants/usersTypes.contant";
import type { IProfile } from "./profiles.interface";

export interface IUsers {
    id: number,
    first_name: string;
    last_name: string;
    email: string;
    password: string;
    profile_id: number;
    access_token: string;
    refresh_token: string;
    user_type: UsersTypes,
    is_root: boolean;

    profile: IProfile;
}