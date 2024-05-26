<script setup lang="ts">
import { ref, onMounted } from 'vue';

const hours = ref('');
const minutes = ref('');
const blink = ref(true);

const updateTime = () => {
  const now = new Date();
  hours.value = String(now.getHours()).padStart(2, '0');
  minutes.value = String(now.getMinutes()).padStart(2, '0');
};

onMounted(() => {
  updateTime();
  setInterval(updateTime, 1000);
  setInterval(() => {
    blink.value = !blink.value;
  }, 1000);
});
</script>

<template>
  <div class="font-bold text-lg">
    {{ hours }}<span class="mx-0.5" :class="{ 'invisible': blink }">:</span>{{ minutes }}
  </div>
</template>