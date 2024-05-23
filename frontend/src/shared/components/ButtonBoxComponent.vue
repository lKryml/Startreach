<template>
	<div
		:class="{
			'border-primary': isActive,
			'border-border': !isActive,
			'bg-accent': isActive
		}"
		@click="emit('change')"
		class="w-auto text-center p-4 rounded-sm border-border border-[1px] flex flex-col justify-center items-center cursor-pointer"
	>
		<img src="../../assets/logo.png" v-show="img" class="w-[36px] mx-2" />
		<!-- <img :src="img" v-show="img" class="w-[36px] mx-2" /> -->
		<!-- <icon size="24" v-show="icon"></icon> -->
		<span class="mb font-semibold">{{ title }}</span>
		<span class="text-sm text-muted" v-show="description">{{ description }}</span>
	</div>
</template>
<script setup lang="ts">
import { defineEmits, defineProps, type PropType } from "vue"

const emit = defineEmits<{ (e: "change"): void }>()
const { isActive } = defineProps({
	isActive: Boolean,
	title: String,
	description: String,
	img: String,
	icon: {
		type: Function as PropType<any>,
		required: false
	}
})
</script>
