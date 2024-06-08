<script lang="ts" setup>
import Icon from "@/shared/components/Icon.vue"
const props = defineProps<{
	title: string
	icon: string
	description?: string
	path?: string
	leanMoreTitle?: string
}>()
</script>
<template>
	<div class="flex flex-col justify-normal items-start p-8">
		<span
			class="w-16 h-16 mb-4 flex justify-center items-center rounded-md bg-white dark:bg-secondary text-orange-400"
			v-if="props.icon"
		>
			<Icon :name="props.icon"></Icon>
		</span>
		<p class="text-xl font-extrabold mb-10">{{ props.title }}</p>
		<p class="mb-4">{{ props.description }}</p>
		<router-link class="hover:underline text-primary" :to="props?.path || ''">{{
			props.leanMoreTitle
		}}</router-link>
	</div>
</template>
