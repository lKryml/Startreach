<template>
	<component :is="icon" />
</template>

<script lang="ts" setup>
import * as icons from "lucide-vue-next"
import { ref, computed, defineProps } from "vue"

const { name } = defineProps({
	name: {
		type: String,
		required: true,
		default: ""
	}
})

const icon = computed(() => (icons as any)[name])
console.log(icon, name)
</script>
