<script setup lang="ts">
import { RecipeCard } from "@/components/ui/recipe";
import { useRecipeStore } from "~/stores/recipeStore";

const recipeStore = useRecipeStore();

const isRecipeDrawerOpened = ref(false);
const openRecipeDrawer = () => {
  isRecipeDrawerOpened.value = true;
};

const title = computed(() =>
  recipeStore.search.lastQuery ? `Результаты по запросу: "${recipeStore.search.lastQuery}"` : "Поиск рецептов");
</script>

<template>
  <Title>{{ title }}</Title>
  <div class="w-full flex justify-between">
    <h2 class="scroll-m-20 text-3xl font-extrabold tracking-tight lg:text-4xl">{{ title }}</h2>
  </div>
  <div v-if="recipeStore.search.recipes?.length > 0"
       class="scrollbar scrollbar-thumb-gray-400 overflow-y-scroll scrollbar-thumb-rounded-full scrollbar-w-2">
    <div class="flex gap-10 flex-wrap justify-center p-4">
      <RecipeCard
        @click="openRecipeDrawer" v-for="recipe in recipeStore.search.recipes" :recipe="recipe" :key="recipe.name"/>
    </div>
  </div>

  <Drawer v-model:open="isRecipeDrawerOpened">
    <DrawerContent>
      <div class="w-full max-w-xl flex justify-start gap-5">
        <RecipeImage :src="recipeStore.selectedRecipe?.image" class="w-1/2"/>
      </div>
    </DrawerContent>
  </Drawer>

</template>