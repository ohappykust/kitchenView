<script setup lang="ts">
import 'ldrs/bouncy';
import {PinPanel} from "~/components/ui/pin-panel";
import { ExclamationTriangleIcon } from '@radix-icons/vue';
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';
import type {IUserPublic} from "~/interfaces/user.interface";

const users = useState<IUserPublic[]>("users");
if (users.value.length === 0 ) navigateTo("/init");

const selected_user_id = ref<number | null>(null);
const set_user_id = async (user_id: number) => {
  selected_user_id.value = user_id;
  if (!selected_user.value?.pin) await login();
};
const clear_user_id = () => selected_user_id.value = null;
const selected_user = computed(() => users.value?.find((u) => u.id === selected_user_id.value));
const loginError = ref<any>(null);

const login = async (pin: string | null = null) => {
  loginError.value = null;
  await $fetch('/users/login', {
    method: 'POST',
    baseURL: useRuntimeConfig().public.baseURL,
    body: {
      id: selected_user_id.value,
      pin: pin
    },
    onResponse({ request, response, options }) {
      if (!response.ok) return;
      localStorage.setItem('access_token', response._data.access_token);
      window.location.reload();
    },
    onResponseError({ request, response, options }) {
      if (response._data?.detail) {
        loginError.value = response._data.detail;
        return;
      }
      loginError.value = "Непредвиденная ошибка.";
    }
  });
};
</script>

<template>
  <Title>Вход</Title>
  <div class="h-full flex justify-center items-center">
    <div>
      <h1 class="scroll-m-20 my-20 text-4xl font-extrabold tracking-tight lg:text-5xl text-center">KitchenView</h1>
      <Suspense>
        <div>
          <div v-if="selected_user_id === null" class="flex gap-12 mb-32 justify-center">
            <div v-for="user in users" @click="set_user_id(user.id)" class="text-center hover:scale-125 transition cursor-pointer">
              <Avatar class="bg-gray-300" size="lg">{{ user.name.toUpperCase()[0] }}</Avatar>
              <h4 class="mt-2 scroll-m-20 text-xl font-semibold tracking-tight">{{ user.name }}</h4>
            </div>
          </div>
          <div v-if="selected_user !== undefined">
            <div class="text-center transition mb-5">
              <Avatar class="bg-gray-300" size="lg">{{ selected_user.name.toUpperCase()[0] }}</Avatar>
              <h4 class="mt-2 scroll-m-20 text-xl font-semibold tracking-tight">{{ selected_user.name }}</h4>
            </div>
            <Alert v-if="loginError" variant="destructive" class="my-6">
              <ExclamationTriangleIcon class="w-4 h-4" />
              <AlertTitle>Ошибка!</AlertTitle>
              <AlertDescription>
                {{ loginError }}
              </AlertDescription>
            </Alert>
            <PinPanel v-if="selected_user.pin" :units-count="4" :on-exit="clear_user_id" :on-complete="login"
                      :clear-after-complete="true"/>
          </div>
        </div>
        <template #fallback>

        </template>
      </Suspense>
    </div>
  </div>
</template>

<style scoped>

</style>