import { enviroment } from "@/enviroments/enviroment"
import type { IPagination } from "@/interfaces/global.interface";
import type { IProjects } from "@/interfaces/project.interface"
import { prepareSearchPagination } from "@/libs/requestify.lib";



export const create = async (_values: IProjects) => (
    fetch(`${enviroment.apiUrl}/api/projects`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(_values)
    }).catch((err) => console.log(err))
);


export const update = async (_values: IProjects) => (
    fetch(`${enviroment.apiUrl}/api/projects/${_values.id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(_values)
    }).catch((err) => console.log(err))
);


export const findById = async (itemId: IProjects['id']) => {
    return fetch(
        `${enviroment.apiUrl}/api/projects/${itemId}`
    ).catch((err) => console.log(err))
};


export const find = async (pagination: IPagination) => {
    return fetch(prepareSearchPagination(
        `${enviroment.apiUrl}/api/projects`,
        pagination)
    ).catch((err) => console.log(err))
};


export const destroy = async (itemId: IProjects['id']) => (
    fetch(`${enviroment.apiUrl}/api/projects/${itemId}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
    }).catch((err) => console.log(err))
);