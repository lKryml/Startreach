<template>
	<div class="flex justify-around flex-col items-center bg-white border-accent">
		<div
			class="grid grid-flow-row grid-rows-3 gap-4 items-center p-4 bg-accent border-b-accent"
		>
			<div v-for="(item, index) in steps" :key="index">
				<span v-bind:class="{ 'bg-primary': index + 1 === currentStep }">{{
					index + 1
				}}</span
				>{{ steps[index] }}
			</div>
		</div>
		<slot class="flex-1"></slot>
		<div class="flex justify-between flex-row items-center p-4 bg-accent border-t-accent">
			<button @click="onStep(1)">Next</button>
			<button @click="onStep(-1)">Previous</button>
		</div>
	</div>
</template>

<script setup lang="ts">
import { ref, defineProps } from "vue"
const { steps, defaultStep } = defineProps({
	steps: {
		type: Array<string>, // step title ['login', 'info', 'etc']
		required: true
	},
	defaultStep: {
		type: Number,
		required: true,
		default: 1
	}
})
const currentStep = ref(defaultStep || 1)
const onStep = (_currentStep: number) => {
	console.log(currentStep.value, _currentStep)
	if (currentStep.value >= steps.length && _currentStep === 1) return
	else if (currentStep.value <= 1 && _currentStep === -1) return

	currentStep.value += _currentStep
	console.log(currentStep.value)
	if (_currentStep === 1) emit("onnext", currentStep.value)
	else emit("onpreviuos", currentStep.value)
}

const emit = defineEmits<{
	(e: "onnext", currentStep: number): void
	(e: "onpreviuos", currentStep: number): void
}>()
</script>
