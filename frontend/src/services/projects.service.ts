import type { IPagination, IResponse } from "@/interfaces/global.interface";
import type { IProjects } from "@/interfaces/projects.interface"
import { prepareSearchPagination } from "@/libs/requestify.lib";
import { HttpClient } from "@/classes/httpClient";

const http = new HttpClient();
export const _controller = 'projects';
export const create = async (_values: IProjects) => {
    return http.create<IProjects>(_controller, _values)
};


export const update = async (_values: IProjects) => {
    return http.update<IProjects>(_controller, _values.id, _values)
};


export const findById = async (itemId: IProjects['id']) => {
    return http.get<IProjects>(_controller, itemId);
};


export const find = async (pagination: IPagination): Promise<IResponse<IProjects[]> | null> => {
    return http.getAll<IProjects>(
        prepareSearchPagination(_controller, pagination,)
    );
};


export const destroy = async (itemId: IProjects['id']) => (
    http.delete(_controller, itemId)
);

export const uploadImage = async (itemId: IProjects['id'] | null, formData: FormData) => {
    return http.create(`${_controller}/images/${itemId || ''}`, formData);
}