<script setup lang="ts">
import { cn } from "@/libs/utils"
import { defineProps } from "vue"
import { Card, CardContent, CardHeader, Button } from "@/shared/shadcn-ui/ui"

export interface CardProps {
	thumbnail?: string
	title: string
	description?: string
	layout?: "vertical" | "horizontal"
	date?: Date
	path?: string
	moreTitle?: string
	votes?: {
		up: number
		down: number
	}
}

const props = defineProps<CardProps>()
const emit = defineEmits<{
	(e: "onclick", $event: any): void
}>()
</script>
<template>
	<Card
		class="w-full h-[300px] flex justify-center items-start"
		v-bind:class="cn(props.layout === 'vertical' ? 'flex-col' : 'flex-row')"
	>
		<CardHeader class="w-full">
			<div
				class="image-golder"
				:class="cn(props.layout === 'vertical' ? 'h-36 w-full' : 'h-full w-1/3')"
				:style="{ backgroundImage: `url('${props.thumbnail}` }"
			></div>
			<!-- <img
				class="min-w-full max-h-full bg-cover"
				v-show="props.thumbnail"
				:src="props.thumbnail"
			/> -->
		</CardHeader>
		<CardContent class="flex flex-col justify-start items-start">
			<div class="w-full text-xl font-bold" @click="($event) => emit('onclick', $event)">
				{{ props.title }}
			</div>
			<!-- <div class="w-full text-ellipsis overflow-hidden">{{ props.description }}</div> -->
			<div class="w-full self-end">{{ props.date?.toDateString() }}</div>
			<router-link v-if="props.path" :to="props.path" class="w-full justify-self-end">
				<Button>{{ props.moreTitle || "More" }}</Button>
			</router-link>
			<slot></slot>
		</CardContent>
	</Card>
</template>
