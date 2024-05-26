<script setup lang="ts">
import { RecipeCard } from "~/components/ui/recipe";
import { useUserStore } from "~/stores/userStore";

import { Search, SquarePen } from "lucide-vue-next";

const userStore = useUserStore();
const user = userStore.user;

const isCreateRecipeDialogOpened = ref<boolean>(false);
</script>

<template>
  <Title>Главная страница</Title>
  <div class="w-full overflow-auto">
    <div class="w-full flex justify-between mb-8">
      <h2 class="scroll-m-20 text-3xl font-extrabold tracking-tight lg:text-4xl">
        Мои рецепты
      </h2>
      <Button @click="isCreateRecipeDialogOpened = true" size="lg" variant="default">Добавить рецепт</Button>
    </div>
    <div v-if="user?.recipes && user.recipes.length > 0" class="flex gap-10 flex-wrap">
      <RecipeCard v-for="recipe in user?.recipes" :recipe="recipe" :key="recipe.name" />
    </div>
    <div v-else class="w-full flex justify-center items-center">
      <div class="flex items-center justify-center w-full">
          <button @click="isCreateRecipeDialogOpened = true" type="button" class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
              <div class="flex flex-col items-center justify-center pt-5 pb-6">
                  <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8 2.75C8 2.47386 7.77614 2.25 7.5 2.25C7.22386 2.25 7 2.47386 7 2.75V7H2.75C2.47386 7 2.25 7.22386 2.25 7.5C2.25 7.77614 2.47386 8 2.75 8H7V12.25C7 12.5261 7.22386 12.75 7.5 12.75C7.77614 12.75 8 12.5261 8 12.25V8H12.25C12.5261 8 12.75 7.77614 12.75 7.5C12.75 7.22386 12.5261 7 12.25 7H8V2.75Z" fill="currentColor" fill-rule="evenodd" clip-rule="evenodd"></path></svg>
                  <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Нажмите, чтобы добавить</span></p>
                  <p class="text-xs text-gray-500 dark:text-gray-400">новый рецепт</p>
              </div>
          </button>
      </div>
    </div>
  </div>

  <!-- TODO: Move this dialog to component -->
  <Dialog v-model:open="isCreateRecipeDialogOpened">
    <DialogContent class="w-full max-w-2xl">
      <DialogHeader>
        <DialogTitle>Добавление рецепта</DialogTitle>
        <DialogDescription>Как вы хотите добавить новый рецепт?</DialogDescription>
      </DialogHeader>
      <div class="w-full flex justify-around my-2">
        <Button disabled variant="outline" class="flex flex-col gap-5 h-72 w-72">
          <SquarePen class="w-16 h-16" />
          <div class="flex flex-col text-wrap gap-2">
            <span class="text-lg font-bold">Создать новый рецепт</span>
            <span class="text-muted-foreground">Свой рецепт. Свои ингредиенты. Свои правила.</span>
          </div>
        </Button>
        <NuxtLink to="/search">
          <Button variant="outline" class="flex flex-col gap-5 h-72 w-72">
            <Search class="w-16 h-16" />
            <div class="flex flex-col text-wrap gap-2">
              <span class="text-lg font-bold">Найти рецепт</span>
              <span class="text-muted-foreground">Поиск среди сторонних сайтов и ресурсов</span>
            </div>
          </Button>
        </NuxtLink>
      </div>
    </DialogContent>
  </Dialog>
</template>
