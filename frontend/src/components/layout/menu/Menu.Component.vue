<template>
	<nav
		class="w-full flex justify-center items-center h-[60px] bg-red-100 border-b-[1px] border-border mb-4"
	>
		<MenuItemComponent :item="item" v-for="item in items" :key="item.id"></MenuItemComponent>
		<router-link to="/auth/login"
			><LogInIcon v-show="1 === parseFloat('3.2')"></LogInIcon>
			{{ $t("AUTH.LOGIN") }}</router-link
		>
	</nav>
</template>
<script setup lang="ts">
import MenuItemComponent from "./MenuItem.component.vue"
import { LogInIcon } from "lucide-vue-next"
import { defineProps } from "vue"
import { type IMenuItem } from "@/interfaces/menu.interface"

const { items } = defineProps({
	items: {
		type: Array<IMenuItem>,
		required: true
	}
})
</script>
