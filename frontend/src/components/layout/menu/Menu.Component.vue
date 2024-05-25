<template>
	<nav class="w-full flex justify-between bg-navbar left-0 t-0 items-center mb-0 fixed top-0">
		<div
			class="w-full container flex justify-between items-center h-[70px] bg-transparent mb-4"
		>
			<div
				class="text-foreground flex justify-center items-center border border-red-600"
			></div>

			<div class="flex justify-end items-center border border-red-600 w-2/4">
				<!-- <img src="../../../assets/logo.png" class="w-9 h-auto max-h-9" /> -->
				<div class="flex justify-between border border-lime-300 w-2/4 pl-36 gap-6">
					<RouterLink to="/"> More </RouterLink>
					<RouterLink to="/"> Projects </RouterLink>
					<RouterLink to="/"> Investors </RouterLink>
					<RouterLink to="/"> Startups </RouterLink>
				</div>

				<Logo />
			</div>
			<slot></slot>
		</div>
	</nav>
</template>
<script setup lang="ts">
import MenuItemComponent from "./MenuItem.component.vue"
import { useI18n } from "vue-i18n"
import { defineProps } from "vue"
import { type IMenuItem } from "@/interfaces/menu.interface"
import Button from "@/shared/shadcn-ui/ui/button/Button.vue"
import Logo from "@/components/svg/Logo.vue"

const { t } = useI18n()
const { items } = defineProps({
	items: {
		type: Array<IMenuItem>,
		required: true
	}
})
</script>
