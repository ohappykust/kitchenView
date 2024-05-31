import type {IUser} from "~/interfaces/user.interface";

export interface IUserStore {
  users: IUser[];
  user: IUser | null;
  userLoadingError: any | null;
  userIsLoading: boolean;
}