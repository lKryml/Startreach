import { enviroment } from "@/enviroments/enviroment"
import type { IUsers } from "@/interfaces/users.interface"


export const register = async (_values: IUsers) => (
    fetch(`${enviroment.apiUrl}/auth/register`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(_values)
    }).catch((err) => console.log(err))
);

export const login = async (_values: IUsers) => (
    fetch(`${enviroment.apiUrl}/auth/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(_values)
    }).catch((err) => console.log(err))
);