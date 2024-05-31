<template>
  <div class="h-screen bg-gray-150 overflow-hidden">
    <NuxtPage v-if='useRouter().currentRoute.value.fullPath.includes("/login")
                    || useRouter().currentRoute.value.fullPath.includes("/init")' />
    <NuxtLayout v-else>
      <Suspense>
        <NuxtPage/>
      </Suspense>
    </NuxtLayout>
  </div>
  <Toaster/>
</template>

<script async setup lang="ts">
import {Toaster} from "~/components/ui/toast";

const userStore = useUserStore();
await userStore.getCurrentUser();
await userStore.getAllUsers();
</script>
