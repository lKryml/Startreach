<template>
	<h1>Root Header Goes Here</h1>
	<router-view />
</template>
<script setup lang="ts">
import { onBeforeMount } from "vue"
onBeforeMount(() => {
	console.log("Check If Authenticated!!")
})
</script>
