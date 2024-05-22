<template>
	<router-view />
	<Toaster />
</template>

<script setup lang="ts">
import { useAuthStore } from "./stores/auth.store"
import { Toaster } from "@/shared/shadcn-ui/ui/toast"

const authStore = useAuthStore()
</script>
