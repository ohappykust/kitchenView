<script setup lang="ts">
import 'ldrs/bouncy';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button'
import { PinPanel } from "~/components/ui/pin-panel";

import type {IUserCreate, IUserPublic} from "~/interfaces/user.interface";

const users = useState<IUserPublic[]>("users");
if (users.value.length > 0 ) navigateTo("/login");

const stage = ref<number>(1);
const loading = ref<boolean>(false);
const user = ref<IUserCreate>({
  name: "",
  pin: null
});
const createError = ref<any>(null);

const stage_title: { [key: number]: Function } = {
  1: () => "Добро пожаловать! Как тебя зовут?",
  2: () => `Приятно познакомиться, ${user.value.name}!`,
  3: () => `${user.value.name}, время придумывать!`
}

const createUser = async (pin: string | null) => {
  loading.value = true;
  if (pin) user.value.pin = pin;
  await $fetch('/users/', {
    method: 'POST',
    baseURL: useRuntimeConfig().public.baseURL,
    body: user.value,
    onResponse({ request, response, options }) {
      if (!response.ok) return;
      window.location.reload();
    },
    onResponseError({ request, response, options }) {
      if (response._data?.detail) {
        createError.value = response._data.detail;
        return;
      }
      createError.value = "Непредвиденная ошибка.";
      loading.value = false;
    }
  });
};
</script>

<template>
  <Title>Добро пожаловать!</Title>
  <div class="h-full flex justify-center items-center">
    <div>
      <h1 class="scroll-m-20 mb-20 text-3xl font-extrabold tracking-tight lg:text-5xl text-center">KitchenView</h1>
      <h2 class="scroll-m-20 my-5 text-xl font-bold tracking-tight lg:text-3xl text-center">{{ stage_title[stage]() }}</h2>

      <Transition>
        <div v-if="stage === 1" class="mx-auto max-w-sm flex flex-wrap items-center justify-center gap-10 w-full">
          <Input v-model="user.name" class="text-center text-xl py-2.5 px-2.5" type="text" placeholder="Твоё прекрасное имя" />
          <Button size="lg" @click="stage += 1">Продолжить</Button>
        </div>
      </Transition>
      <div v-if="stage === 2" class="w-full">
        <h2 v-if="stage === 2" class="scroll-m-20 mb-10 font-bold tracking-tight text-xl text-center">
          Хочешь установить пин-код?
        </h2>
        <div class="flex gap-10 justify-center">
          <Button :disabled="loading" variant="outline" size="lg" @click="createUser">Не сейчас</Button>
          <Button :disabled="loading" variant="default" size="lg" @click="stage += 1">Хочу</Button>
        </div>
      </div>
      <div v-if="stage === 3">
        <PinPanel :on-complete="createUser" :units-count="4" />
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>