<script setup lang="ts">
import { defineProps, defineEmits } from "vue"
import {
	Card,
	CardContent,
	CardDescription,
	CardFooter,
	CardHeader,
	CardTitle,
	Button
} from "@/shared/shadcn-ui/ui/"
interface IntroducerProps {
	title: string
	description: string
	addTitle?: string
	image?: string
}

const props = defineProps<IntroducerProps>()
const emit = defineEmits<{ (e: "onaddnew"): void }>()
</script>
<template>
	<div class="flex items-start">
		<Card class="flex-1 flex flex-col justify-center items-center">
			<CardHeader class="pb-3">
				<CardTitle>{{ props.title }}</CardTitle>
			</CardHeader>
			<CardContent class="flex flex-col justify-center items-center">
				<CardDescription class="max-w-lg text-balance leading-relaxed">{{
					props.description
				}}</CardDescription>
				<img
					class="rounded-full w-[200px]"
					v-if="props.image"
					:src="props.image"
					:alt="props.title"
				/>
			</CardContent>
			<CardFooter v-if="props.addTitle" class="mb-4">
				<Button variant="secondary"
					><span class="w-full h-full m-0 p-0" @click="emit('onaddnew')">{{
						props.addTitle
					}}</span></Button
				>
			</CardFooter>
		</Card>
	</div>
</template>
