<script setup lang="ts">
import type {IRecipeNutritionInfo} from "~/interfaces/recipe.interface";

defineProps<{
  nutritionInfo: IRecipeNutritionInfo
}>()
</script>

<template>
<div class="flex justify-center gap-5">
  <div class="flex flex-col text-center">
    <span class="font-bold">{{nutritionInfo.kilocalories}}</span>
    <span class="uppercase text-muted-foreground !text-sm font-semibold">Ккал</span>
  </div>
  <div class="flex flex-col text-center">
    <span class="font-bold">{{nutritionInfo.fats}}</span>
    <span class="uppercase text-muted-foreground !text-sm font-semibold">Жиров</span>
  </div>
  <div class="flex flex-col text-center">
    <span class="font-bold">{{nutritionInfo.proteins}}</span>
    <span class="uppercase text-muted-foreground !text-sm font-semibold">Белков</span>
  </div>
  <div class="flex flex-col text-center">
    <span class="font-bold">{{nutritionInfo.carbohydrates}}</span>
    <span class="uppercase text-muted-foreground !text-sm font-semibold">Углеводов</span>
  </div>
</div>
</template>