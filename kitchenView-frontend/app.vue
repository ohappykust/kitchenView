<template>
  <div class="h-screen bg-gray-150 overflow-hidden">
    <NuxtPage v-if='useRouter().currentRoute.value.fullPath.includes("/login") || useRouter().currentRoute.value.fullPath.includes("/init")' />
    <NuxtLayout v-else>
      <NuxtPage/>
    </NuxtLayout>
  </div>
  <Toaster/>
</template>

<script setup lang="ts">
import {Toaster} from "~/components/ui/toast";
import useAuthedFetch from "~/extensions/useAuthedFetch";
import type {IUserPublic} from "@/interfaces/user.interface";

const userStore = useUserStore();
await userStore.getCurrentUser();

const users = useState<IUserPublic[] | null>('users');
await callOnce(async () => {
  const { data } = await useAsyncData<IUserPublic[] | null>(
    'users',
    () => useAuthedFetch('/users/')
  );
  users.value = data.value;
})
</script>
