<template>
	<Dialog>{{ r }}</Dialog>
	<Input type="text" placeholder="email@test.com" />
</template>
<script lang="ts">
import { defineComponent } from "vue"
import { Input } from "@shadcn/ui/input"
import { Dialog } from "@shadcn/ui/dialog"

export default defineComponent({
	setup() {},
	components: {
		Input,
		Dialog
	},
	data: () => {
		return {
			r: "dsadads"
		}
	}
})
</script>
