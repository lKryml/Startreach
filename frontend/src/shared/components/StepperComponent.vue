<template>
	<div
		class="flex border-[1px] border-border justify-start flex-col items-stretch bg-white w-full"
	>
		<div
			class="w-full grid grid-flow-row grid-cols-3 gap-4 items-center p-4 border-b-[1px] border-b-accent"
		>
			<div v-for="(item, index) in steps" :key="index">
				<span
					class="w-8 h-8 rounded-full cursor-pointer bg-primary text-primary-foreground"
					v-bind:class="{ 'bg-primary': index + 1 === currentStep }"
					>{{ index + 1 }}</span
				>{{ steps[index] }}
			</div>
		</div>
		<slot class="flex-1"></slot>
		<div
			class="w-full flex justify-between flex-row-reverse items-center p-4 border-t-[1px] border-t-accent"
		>
			<button v-show="currentStep === steps?.length" type="submit">{{ finishTitle }}</button>
			<button v-show="currentStep !== steps?.length" @click="onStep(1)">
				{{ nextTitle }}
			</button>
			<button @click="onStep(-1)" :disabled="currentStep === 0">{{ prevTitle }}</button>
		</div>
	</div>
</template>

<script setup lang="ts">
import { ref, defineProps } from "vue"
const { steps, defaultStep } = defineProps({
	nextTitle: { type: String, default: "Next" },
	prevTitle: { type: String, default: "Previous" },
	finishTitle: { type: String, default: "Finish" },
	steps: { type: Array<string>, required: true },
	defaultStep: { type: Number, required: true, default: 1 }
})
const currentStep = ref(defaultStep || 1)
const onStep = (_currentStep: number) => {
	console.log(currentStep.value, _currentStep)
	if (currentStep.value >= steps.length && _currentStep === 1) return
	else if (currentStep.value <= 1 && _currentStep === -1) return

	currentStep.value += _currentStep
	if (_currentStep === 1) emit("onnext", currentStep.value)
	else emit("onpreviuos", currentStep.value)
}

const emit = defineEmits<{
	(e: "onnext", currentStep: number): void
	(e: "onpreviuos", currentStep: number): void
	(e: "onfinish", currentStep: number): void
}>()
</script>
