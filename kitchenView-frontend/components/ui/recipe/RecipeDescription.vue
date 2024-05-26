<script setup lang="ts">
import {Dot, TimerReset, User} from "lucide-vue-next";

import type {IRecipe} from "~/interfaces/recipe.interface";
import { getPortionsWord, getTimeWords } from "~/lib/utils";

defineProps<{
  recipe: IRecipe
}>();
</script>

<template>
<div class="flex flex-col gap-2">
  <div class="flex gap-2">
    <div>{{ recipe.category ? `${recipe.category}` : "Неизвестная категория" }}</div>
    <span>|</span>
    <div>{{ recipe.kitchen ? recipe.kitchen : "Неизвестная кухня" }}</div>
  </div>
  <div class="flex">
    <div class="flex"><User class="h-5 w-5 mr-1"/>{{ getPortionsWord(recipe.portions_count) }}</div>
    <Dot class="w-5 h-5" />
    <div class="flex"><TimerReset class="h-5 w-5 mr-1"/> {{ getTimeWords(recipe.cooking_time_minutes) }} </div>
  </div>
</div>
</template>