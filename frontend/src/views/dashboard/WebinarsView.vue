<
<script setup lang="ts">
// import * as projectsService from "@/services/projects.service"
// import type { IProjects } from "@/interfaces/project.interface"
import ItemCard from "@/components/ui/ItemCard.vue"
import {
	// Table,
	// TableBody,
	// TableCaption,
	// TableCell,
	// TableHead,
	// TableHeader,
	// TableRow,
	DropdownMenu,
	DropdownMenuGroup,
	DropdownMenuItem,
	DropdownMenuContent,
	DropdownMenuTrigger,
	DropdownMenuSeparator
} from "@/shared/shadcn-ui/ui"
import PanelTitle from "@/components/layout/menu/PanelTitle.vue"
import { useI18n } from "vue-i18n"
import { DotsHorizontalIcon } from "@radix-icons/vue"
import { onBeforeMount } from "vue"
import type { IPagination } from "@/interfaces/global.interface"
import { ref } from "vue"

const { t } = useI18n()
const pagination: IPagination = {
	page: 1,
	per_page: 20,
	sort: "desc",
	sortBy: "id",
	queries: "",
	search: ""
}
const projects = ref<IProjects[]>([])
onBeforeMount(async () => {
	const response = await projectsService.find(pagination)
	if (response?.ok) {
		const jsonResponse = response?.json ? await response.json() : undefined
		projects.value = jsonResponse.data || []
		console.log(projects, jsonResponse)
	} else {
		console.log(response)
	}
})
</script>

<template>
	<div class="border-amber-200 border flex h-full w-full flex-col">
		<PanelTitle v-bind:title="t('MENU.PROJECTS')"></PanelTitle>
		<div class="flex flex-row flex-wrap overflow-auto gap-4">
			<ItemCard
				v-for="project in projects"
				:key="project.id"
				class="w-[250px]"
				layout="vertical"
				:thumbnail="project.img"
				:title="project.name"
				:description="project.description"
				:votes="{ up: 22, down: 2 }"
				:date="new Date()"
			>
			</ItemCard>
		</div>
	</div>
</template>
