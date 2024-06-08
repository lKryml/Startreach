<template>
	<nav class="w-full flex justify-end bg-navbar left-0 t-0 mb-0 fixed top-0">
		<div
			class="w-full flex justify-end items-center h-[70px] bg-transparent mb-4 ml-24"
		>
			<div class="btn-area ">
				<a>Learn more</a>
			</div>
			
			<div class="flex justify-end items-center border border-red-600 w-2/4 m-0">
				<!-- <img src="../../../assets/logo.png" class="w-9 h-auto max-h-9" /> -->
				<div class="flex justify-between  w-2/4 pl-16 gap-6">
					<RouterLink to="/"> More </RouterLink>
					<RouterLink to="/"> Projects </RouterLink>
					<RouterLink to="/"> Investors </RouterLink>
					<RouterLink to="/"> Startups </RouterLink>
				</div>

				<Logo />
			</div>
		</div>
	</nav>
</template>
<script setup lang="ts">
import MenuItemComponent from "./MenuItem.component.vue"
import { useI18n } from "vue-i18n"
import { defineProps } from "vue"
import { type IMenuItem } from "@/_interfaces/menu.interface"
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
