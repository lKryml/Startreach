<script setup lang="ts">
import { Button } from "@/shared/shadcn-ui/ui/button"
const onclickme = () => {
	confirm("Are u human?!!")
}
</script>
<template>
	<Button
		><span class="w-full h-full m-0 p-0" @click="() => onclickme()">Hello Human</span></Button
	>
</template>
