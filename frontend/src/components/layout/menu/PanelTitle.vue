<template>
	<div class="grid grid-cols-2 grid-flow-row w-full p-10">
		<div class="flex justify-start items-center">
			<img v-show="icon" :src="icon" class="w-10 h-10 me-2" />
			<h2 class="text-3xl font-extrabold">{{ title }}</h2>
		</div>
	</div>
</template>
<script setup lang="ts">
export interface PanelTitleProps {
	title: string
	icon?: string
}
defineProps<PanelTitleProps>()
</script>
