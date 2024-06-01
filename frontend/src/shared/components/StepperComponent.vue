<template>
	<div
		class="flex border-[1px] border-border justify-start flex-col items-stretch bg-white w-full"
	>
		<div
			class="w-full grid grid-flow-row grid-cols-3 gap-4 items-center p-4 border-b-[1px] border-b-accent"
		>
			<div
				class="cursor-pointer w-auto h-full flex justify-start items-center p-2 bg-dashboard text-dashboard-foreground rounded-md"
				v-for="(item, index) in steps"
				:key="index"
			>
				<span
					class="w-6 h-6 me-1 rounded-full cursor-pointer flex justify-center items-center"
					v-bind:class="{
						'bg-primary': index + 1 === currentStep,
						'text-primary-foreground': index + 1 === currentStep
					}"
					>{{ index + 1 }}</span
				>
				{{ steps[index] }}
			</div>
		</div>
		<slot class="flex-1"></slot>
		<div
			class="w-full flex justify-between flex-row-reverse items-center p-4 border-t-[1px] border-t-accent"
		>
			<Button variant="secondary" v-show="currentStep === steps?.length" type="submit">
				<span class="w-full h-full m-0 p-0" v-if="!loading">{{ finishTitle }}</span>
				<Loader2Icon v-else class="w-8 h-8 me-2 animate-spin" />
			</Button>
			<Button variant="secondary" v-show="currentStep !== steps?.length" @click="onStep(1)">
				{{ nextTitle }}
			</Button>
			<Button variant="secondary" @click="onStep(-1)" :disabled="currentStep === 0">{{
				prevTitle
			}}</Button>
		</div>
	</div>
</template>

<script setup lang="ts">
import { ref, defineProps } from "vue"
import { Button } from "@/shared/shadcn-ui/ui"
const { steps, defaultStep } = defineProps({
	nextTitle: { type: String, default: "Next" },
	prevTitle: { type: String, default: "Previous" },
	finishTitle: { type: String, default: "Finish" },
	steps: { type: Array<string>, required: true },
	defaultStep: { type: Number, required: true, default: 1 },
	loading: { rtpe: Boolean, default: false }
})
const currentStep = ref(defaultStep || 1)
const onStep = (_currentStep: number) => {
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
