import type {IRecipe} from "~/interfaces/recipe.interface";

export interface IUserTokens {
    access_token: string
}

export interface IUserPublic {
    id: number,
    name: string,
    pin: boolean | null
}

export interface IUser extends IUserPublic {
    recipes: IRecipe[],
    is_admin: boolean
}

export interface IUserCreate {
    name: string,
    pin: string | null
}

export interface IUserLogin {
    id: number,
    pin: string | null
}