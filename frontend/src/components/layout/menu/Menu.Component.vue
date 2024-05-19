<template>
	<nav class="w-full flex justify-between items-center bg-transparent mb-4">
		<div
			class="w-full container flex justify-between items-center h-[70px] bg-transparent mb-4"
		>
			<div class="text-foreground flex justify-center items-center">
				<Button
					class="rounded-full shadow-none w-48 h-10 bg-secondary text-secondary-foreground"
					>{{ t("GENERAL.CONTACT_US") }}</Button
				>
			</div>
			<div class="flex-1 flex justify-center items-center">
				<MenuItemComponent
					:item="item"
					v-for="item in items"
					:key="item.id"
				></MenuItemComponent>
			</div>
			<!-- <router-link to="/auth/login"
				><LogInIcon v-show="1 === parseFloat('3.2')"></LogInIcon>
				{{ $t("AUTH.LOGIN") }}</router-link
			> -->
			<div class="flex justify-self-end items-center">
				<img src="../../../assets/logo.png" class="w-9 h-auto max-h-9" />
			</div>
		</div>
	</nav>
</template>
<script setup lang="ts">
import MenuItemComponent from "./MenuItem.component.vue"
import { useI18n } from "vue-i18n"
import { defineProps } from "vue"
import { type IMenuItem } from "@/interfaces/menu.interface"
import Button from "@/shared/shadcn-ui/ui/button/Button.vue"

const { t } = useI18n()
const { items } = defineProps({
	items: {
		type: Array<IMenuItem>,
		required: true
	}
})
</script>
