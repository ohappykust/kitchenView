<script setup lang="ts">
import type {IRecipe} from "~/interfaces/recipe.interface";
import { RecipeNutritionInfo, RecipeDescription, RecipeImage } from ".";

defineProps<{
  recipe: IRecipe
}>()
</script>

<template>
  <Card class="w-96 hover:cursor-pointer hover:scale-105 shadow transition ease-in-out flex flex-col justify-between">
    <CardHeader>
      <CardTitle>{{ recipe.name }}</CardTitle>
      <CardDescription>
        <RecipeDescription :recipe="recipe" />
      </CardDescription>
    </CardHeader>
    <CardContent class="my-auto">
      <RecipeImage :src="recipe.image_url" :alt="recipe.name" />
    </CardContent>
    <CardFooter class="w-full flex justify-center">
      <RecipeNutritionInfo :nutrition-info="recipe.nutrition_info" />
    </CardFooter>
  </Card>
</template>