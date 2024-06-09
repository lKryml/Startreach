<script setup lang="ts">
import { Button } from "@/shared/shadcn-ui/ui/button"
import {
	Card,
	CardContent,
	CardDescription,
	CardFooter,
	CardHeader,
	CardTitle
} from "@/shared/shadcn-ui/ui/card"
import { useI18n } from "vue-i18n"
import PanelTitle from "@/components/menu/PanelTitle.vue"

const { t } = useI18n()
</script>
<template>
	<main class="container py-10">
		<PanelTitle
			v-bind:title="t('MENU.DASHBOARD')"
			:is-breadcrumb="true"
			:breadcrumb-links="[{ path: '', label: t('MENU.DASHBOARD') }]"
		></PanelTitle>
		<div class="grid auto-rows-max items-start gap-4 md:gap-8 lg:col-span-2">
			<div class="grid gap-4 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-2 xl:grid-cols-4">
				<Card>
					<CardHeader class="pb-2">
						<CardDescription>{{ t("PROJECTS.PAGE_TITLE") }}</CardDescription>
						<CardTitle class="text-4xl"> 3 </CardTitle>
					</CardHeader>
					<CardContent>
						<!-- <div class="text-xs text-muted-foreground"></div> -->
					</CardContent>
				</Card>
				<Card>
					<CardHeader class="pb-2">
						<CardDescription>{{ t("WEBINARS.PAGE_TITLE") }}</CardDescription>
						<CardTitle class="text-4xl"> 5 </CardTitle>
					</CardHeader>
					<CardContent>
						<!-- <div class="text-xs text-muted-foreground"></div> -->
					</CardContent>
				</Card>
			</div>
		</div>
	</main>
</template>
