<template>
	<div class="flex w-full justify-center items-center">
		<MenuComponent :items="menuItems" />
	</div>
	<router-view />
</template>

<script setup lang="ts">
import { menu } from "@/constants/menu/public.menu"
import MenuComponent from "@/components/layout/menu/Menu.Component.vue"
const menuItems = menu
console.log(menuItems)
</script>
