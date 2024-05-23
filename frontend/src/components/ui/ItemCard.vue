<script setup lang="ts">
import { cn } from "@/libs/utils"
import { defineProps } from "vue"
import { Card, CardContent, CardHeader } from "@/shared/shadcn-ui/ui"

export interface CardProps {
	thumbnail: string
	title: string
	description: string
	layout: "vertical" | "horizontal"
	date: Date
	votes: {
		up: number
		down: number
	}
}

const props = defineProps<CardProps>()
</script>
<template>
	<Card
		class="w-full h-[300px] flex justify-center items-start"
		v-bind:class="cn(props.layout === 'vertical' ? 'flex-col' : 'flex-row')"
	>
		<CardHeader>
			<img
				class="min-w-full max-h-full bg-cover"
				v-show="props.thumbnail"
				:src="props.thumbnail"
			/>
		</CardHeader>
		<CardContent class="flex flex-col justify-between items-start">
			<CardTitle class="text-xl font-bold">{{ props.title }}</CardTitle>
			<CardDescription>{{ props.description }}</CardDescription>
			<Button>Hello</Button>
		</CardContent>
	</Card>
</template>
