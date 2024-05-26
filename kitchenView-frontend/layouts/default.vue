<script setup lang="ts">
import { CircleUser, Home, Menu, Search, LoaderCircle, DoorOpen } from 'lucide-vue-next';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Clock } from "~/components/ui/clock";
import { Sheet, SheetContent, SheetTrigger } from '@/components/ui/sheet';

import { useRouter } from "vue-router";

const router = useRouter();
const userStore = useUserStore();
const recipeStore = useRecipeStore();
const searchValue = ref<string>("");

const search = async () => {
  if (!router.currentRoute.value.path.includes("/search")) navigateTo("/search");
  await recipeStore.searchRecipe(searchValue.value);
};
</script>

<template>
  <div class="grid min-h-screen w-full md:grid-cols-[220px_1fr] lg:grid-cols-[280px_1fr]">
    <div class="hidden border-r bg-muted/40 md:block">
      <div class="flex h-full max-h-screen flex-col gap-2">
        <div class="flex justify-between text-xl h-14 items-center border-b px-4 lg:h-[60px] lg:px-6">
          <a href="/" class="flex items-center gap-2 font-semibold">
            <span>KitchenView</span>
          </a>
          <Clock />
        </div>
        <div class="flex-1">
          <nav class="grid items-start p-2 text-sm font-medium lg:px-4">
            <NuxtLink
              to="/"
              class="flex items-center gap-3 rounded-lg px-3 py-3 text-muted-foreground transition-all hover:text-primary"
            >
              <Home class="h-6 w-6" />
              Главная
            </NuxtLink>
            <NuxtLink
              to="/search"
              class="flex items-center gap-3 rounded-lg px-3 py-3 text-muted-foreground transition-all hover:text-primary"
            >
              <Search class="h-6 w-6" />
              Поиск рецептов
            </NuxtLink>
          </nav>
        </div>
        <div class="mt-auto p-4">
          <Button @click="userStore.logout" variant="outline" class="w-full text-start py-8 px-2.5" size="lg">
            <span class="w-full text-end px-2">
              <DoorOpen />
            </span>
            <span class="absolute w-full text-center">Выйти</span>
          </Button>
        </div>
      </div>
    </div>
    <div class="flex flex-col">
      <header class="flex h-14 items-center gap-4 border-b bg-muted/40 px-4 lg:h-[60px] lg:px-6">
        <Sheet>
          <SheetTrigger as-child>
            <Button
              variant="outline"
              size="icon"
              class="shrink-0 md:hidden"
            >
              <Menu class="h-5 w-5" />
              <span class="sr-only">Toggle navigation menu</span>
            </Button>
          </SheetTrigger>
          <SheetContent side="left" class="flex flex-col">
            <nav class="grid gap-2 text-lg font-medium">
              <NuxtLink to="/" class="flex items-center gap-2 text-lg font-semibold">
                <span>KitchenView</span>
              </NuxtLink>
              <NuxtLink to="/" class="mx-[-0.65rem] flex items-center gap-4 rounded-xl px-3 py-2 text-muted-foreground hover:text-foreground">
                <Home class="h-5 w-5" />
                Главная
              </NuxtLink>
              <NuxtLink to="/search" class="mx-[-0.65rem] flex items-centser gap-4 rounded-xl px-3 py-2 text-muted-foreground hover:text-foreground">
              <Search class="h-5 w-5" />
              Поиск рецептов
            </NuxtLink>
            </nav>
            <div class="mt-auto">
              <Button @click="userStore.logout" variant="outline" class="w-full text-start py-8 px-2.5" size="lg">
                <span class="w-full text-end px-2">
                  <DoorOpen />
                </span>
                <span class="absolute w-full text-center">Выйти</span>
              </Button>
            </div>
          </SheetContent>
        </Sheet>
        <div class="w-full flex-1">
          <form @submit.prevent="search">
            <div class="relative flex items-center">
              <Search class="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
              <Input
                type="search"
                v-model="searchValue"
                placeholder="Поиск рецептов..."
                :disabled="recipeStore.search.recipesIsLoading"
                class="w-full appearance-none bg-background pl-8 shadow-none md:w-2/3 lg:w-1/3"
              />
              <Button type="button" :disabled="recipeStore.search.recipesIsLoading" @click="search" class="ml-5" size="lg" variant="default">
                <LoaderCircle v-if="recipeStore.search.recipesIsLoading" class="w-4 h-4 mr-2 animate-spin" />
                Поиск
              </Button>
            </div>
          </form>
        </div>
        <div class="flex justify-center items-center gap-5 select-none">
          <TooltipProvider class="hover:cursor-help">
            <Tooltip>
              <TooltipTrigger as-child>
                <span>{{ userStore.user?.name }}</span>
              </TooltipTrigger>
              <TooltipContent>
                <p>Вы великолепны!</p>
              </TooltipContent>
            </Tooltip>
          </TooltipProvider>
          <Button variant="secondary" size="icon" class="rounded-full cursor-default">
            <CircleUser class="h-5 w-5" />
            <span class="sr-only">Toggle user menu</span>
          </Button>
        </div>
      </header>
      <main class="flex flex-col gap-4 p-6 lg:gap-6 lg:p-8 max-h-[calc(100vh-60px)]">
        <slot/>
      </main>
    </div>
  </div>
</template>