<script setup lang="ts">
import { Button } from '@/components/ui/button'

const props = defineProps<{
  onInput: Function,
  onExit: Function | null,
  onBackspace: Function
}>()
</script>

<template>
<div class="grid grid-cols-3 grid-rows-4 mt-5 gap-4 justify-items-center">
  <Button class="rounded-2xl text-xl" @click="props.onInput(num+1)" v-for="num in [...Array(9).keys()]" variant="outline" size="cube">{{ num+1 }}</Button>
  <Button v-if="onExit !== null" class="rounded-2xl text-xl" variant="outline" size="cube" @click="props.onExit">
    <span class="material-symbols-outlined">group</span>
  </Button>
  <Button class="rounded-2xl text-xl" @click="props.onInput(0)" variant="outline" size="cube">0</Button>
  <Button class="rounded-2xl text-xl" variant="outline" size="cube" @click="props.onBackspace">
    <span class="material-symbols-outlined ml-2">arrow_back_ios</span>
  </Button>
</div>
</template>