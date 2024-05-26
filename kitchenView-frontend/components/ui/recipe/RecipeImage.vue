<script setup lang="ts">
import {cn} from "~/lib/utils";
import type {HtmlHTMLAttributes} from "vue";

const baseClasses = "w-full h-64 object-cover transition-all hover:scale-105 aspect-[3/4] brightness-75";

const props = defineProps<{
  src: string | null,
  alt: string,
  class?: HtmlHTMLAttributes['class']
}>();
</script>

<template>
<div class="overflow-hidden rounded-md">
  <img
    v-if="src"
    :src="src"
    :alt="alt"
    :class="cn(baseClasses, props.class)"
  >
  <div v-else :class="cn(baseClasses, 'bg-gray-500', props.class)"></div>
</div>
</template>
