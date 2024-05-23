<template>
	<div class="flex w-full justify-center items-center">
		<MenuComponent :items="menu" />
	</div>
	<router-view />
</template>

<script setup lang="ts">
import { menu } from "@/constants/menu/public.menu"
import MenuComponent from "@/components/layout/menu/Menu.Component.vue"
</script>
