<script setup lang="ts">
import { ref, watch, defineEmits } from "vue"
const content = ref<string>()
const emit = defineEmits<{
	(event: "onchange", content: string): void
}>()
watch(content, () => {
	emit("onchange", content.value as string)
})
</script>
<template>
	<QuillEditor v-model:content="content" contentType="html" theme="snow" toolbar="minimal" />
</template>
