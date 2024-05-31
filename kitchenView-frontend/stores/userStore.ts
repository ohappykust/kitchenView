import { defineStore } from "pinia";

import useAuthedFetch from "~/extensions/useAuthedFetch";

import type { IUserStore } from "~/stores/interfaces/userStore.interface";
import type { IUser, IUserTokens } from "~/interfaces/user.interface";

export const useUserStore = defineStore('user', {
  state: (): IUserStore => ({
    users: [],
    usersIsLoading: false,
    usersLoadingError: null,
    user: null,
    userLoadingError: null,
    userIsLoading: false,
  }),
  getters: {
    isLoggedIn: () => localStorage.getItem("access_token") != null,
  },
  actions: {
    async getCurrentUser() {
      this.userIsLoading = true;
      try {
        this.user = await useAuthedFetch<IUser>('/users/me');
      } catch (error) {
        this.userLoadingError = error;
      }
      this.userIsLoading = false;
    },
    async getAllUsers() {
      this.usersIsLoading = true;
      try {
        this.users = await useAuthedFetch<IUser[]>('/users');
      } catch (error) {
        this.usersLoadingError = error;
      }
      this.usersIsLoading = false;
    },
    async logout() {
      this.clearLocalStorage();
      window.location.reload();
    },
    async setUserTokens(tokens: IUserTokens) {
      localStorage.setItem("access_token", tokens.access_token);
    },
    clearLocalStorage() {
      localStorage.removeItem("access_token");
    }
  },
})