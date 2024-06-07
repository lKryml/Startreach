<template>
	<component :is="icon" />
</template>

<script lang="ts" setup>
import * as icons from "lucide-vue-next"
import { computed, defineProps } from "vue"

const { name } = defineProps({
	name: {
		type: String,
		required: true,
		default: ""
	}
})

const icon = computed(() => (icons as any)[name])
</script>
