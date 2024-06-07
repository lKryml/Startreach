<template>
	<div class="container-lg">
	<div class="flex w-full justify-center items-center align-self-end">
		<MenuComponent :items="menu" />
	</div>
	<router-view />
	</div>
</template>

<script setup lang="ts">
import { menu } from "@/constants/menu/public.menu"
import MenuComponent from "@/components/layout/menu/Menu.Component.vue"
</script>
