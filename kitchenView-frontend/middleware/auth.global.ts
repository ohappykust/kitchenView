import { useUserStore } from "~/stores/userStore";

export default defineNuxtRouteMiddleware((to, from) => {
  const isLoggedIn = useUserStore().isLoggedIn;
  if (!["/login", "/init"].includes(to.path) && !isLoggedIn) {
    return navigateTo("/login");
  }
  if (["/login", "/init"].includes(to.path)  && isLoggedIn) {
    return navigateTo("/");
  }
})