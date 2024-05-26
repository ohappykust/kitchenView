import type {IUser} from "~/interfaces/user.interface";

export interface IUserStore {
  user: IUser | null;
  userLoadingError: any | null;
  userIsLoading: boolean;
}