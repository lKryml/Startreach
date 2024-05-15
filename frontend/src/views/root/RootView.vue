<template>
	<h1>Hello From Root Control Panel {{ msg }}</h1>
</template>
<script lang="ts">
import { defineComponent } from "vue"

export default defineComponent({
	beforeMount() {
		console.log("Check If Authenticated!!")
	},
	data: () => {
		return { msg: "fdsf sdf dsf" }
	},
	setup: () => {
		return {}
	}
})
</script>
