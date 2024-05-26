<script setup lang="ts">
import {ref} from 'vue';
import {
  PinInput,
  PinInputGroup,
  PinInputInput,
} from '@/components/ui/pin-input';
import {PinPad} from "@/components/ui/pin-pad";

const props = withDefaults(defineProps<{
  unitsCount: number,
  onComplete: Function,
  onExit: Function | null,
  clearAfterComplete: boolean
}>(), {
  onExit: null,
  clearAfterComplete: false,
})

const value = ref<string[]>([]);
const handleComplete = async (e: string[]) => {
  props.onComplete(e.join(''));
  if (props.clearAfterComplete) value.value = [];
};
const handleInput = (v: number) => value.value.push(v.toString());
const handleBackspace = () => value.value.pop();
</script>

<template>
  <div>
    <PinInput
      id="pin-input"
      v-model="value"
      placeholder="○"
      @complete="handleComplete"
      class="justify-center"
    >
      <PinInputGroup>
        <PinInputInput
          v-for="(id, index) in props.unitsCount"
          :key="id"
          :index="index"
          type="password"
        />
      </PinInputGroup>
    </PinInput>
    <PinPad :on-exit="props.onExit" :on-backspace="handleBackspace" :on-input="handleInput"/>
  </div>
</template>
