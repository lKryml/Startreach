<template>
	<Dialog>{{ r }}</Dialog>
	<Input type="text" placeholder="email@test.com" />
</template>
<script setup lang="ts">
import { Input } from "@shadcn/ui/input"
import { Dialog } from "@shadcn/ui/dialog"
import { ref } from "vue"

const r = ref("Dialog Testing")
</script>
