<template>
	<div class="grid grid-cols-2 grid-flow-row">
		<div class="flex justify-center items-start px-5">
			<img v-show="icon" :src="icon" class="w-10 h-10 me-2" />
			<h2>{{ title }}</h2>
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
