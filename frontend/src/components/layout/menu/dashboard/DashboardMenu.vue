<template>
	<nav
		class="w-full flex justify-between bg-dashboard-navbar text-dashboard-navbar-foreground items-center"
	>
		<div
			class="w-full px-5 border-b-[1px] border-b-border flex justify-start items-center h-[var(--dashboard-navbar-height)]"
		>
			<div class="flex-1 flex justify-start items-center">
				<MenuItemComponent
					:item="item"
					v-for="item in items"
					:key="item.id"
				></MenuItemComponent>
			</div>
			<DashboardAccount />
			<slot></slot>
		</div>
	</nav>
</template>
<script setup lang="ts">
import MenuItemComponent from "../MenuItem.component.vue"
import DashboardAccount from "./DashboardAccount.vue"
import { defineProps } from "vue"
import { type IMenuItem } from "@/_interfaces/menu.interface"
// import { useI18n } from "vue-i18n"

// const { t } = useI18n()
const { items } = defineProps({
	items: {
		type: Array<IMenuItem>,
		required: true
	}
})
</script>
