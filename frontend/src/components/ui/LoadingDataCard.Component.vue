<script setup lang="ts">
import { Card, CardDescription, CardTitle } from "@/shared/shadcn-ui/ui"
import { Loader2Icon } from "lucide-vue-next"

interface LoadingProps {
	loadingTitle: string
}

const { loadingTitle } = defineProps<LoadingProps>()
</script>
<template>
	<Card class="flex flex-col ga-2 justify-center items-center h-96 w-full">
		<CardTitle class="font-bold text-2xl mb-4">{{ loadingTitle }}</CardTitle>
		<CardDescription
			><Loader2Icon class="w-12 h-12 animate-spin text-primary"
		/></CardDescription>
	</Card>
</template>
