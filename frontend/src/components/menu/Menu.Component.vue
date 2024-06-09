<template>
	<nav class="w-full flex justify-start bg-transparent left-0 t-0 mb-0 fixed top-0 border-b-2 border-gray-200 border-opacity-20  backdrop-blur-md ">
		<div
			class="w-full flex justify-start items-center h-[50px] bg-transparent mb-4 ml-24 mt-4 "
		>
			
			<div class="flex justify-between w-full items-center">
			<div class="flex justify-start items-center  w-2/4 m-0">
				<Logo />
				<!-- <img src="../../../assets/logo.png" class="w-9 h-auto max-h-9" /> -->
				<div class="flex justify-between  w-2/4 pl-16 gap-6">
					<RouterLink to="/"> Startups </RouterLink>
					<RouterLink to="/"> Investors </RouterLink>
					<RouterLink to="/projects"> Projects </RouterLink>
					<RouterLink to="/"> More </RouterLink>
				</div>
			</div>
			<div class="btn-area flex gap-8 mr-10 ">
				<a class="cursor-pointer">Learn more</a>
				<a class="cursor-pointer">Sign up</a>
			</div>
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
import Logo from "@/components/Logo.vue"

const { t } = useI18n()
const { items } = defineProps({
	items: {
		type: Array<IMenuItem>,
		required: true
	}
})
</script>
