<template>
	<div class="container-lg">
		<div class="flex w-full justify-center items-center align-self-end">
			<MenuComponent :items="menu" />
		</div>
		<router-view />
		<HomeFooterComponent />
	</div>
</template>

<script setup lang="ts">
import { menu } from "@/constants/menu/public.menu"

import MenuComponent from "@/components/menu/Menu.Component.vue"
import HomeFooterComponent from "@/components/HomeFooter.Component.vue"
</script>
