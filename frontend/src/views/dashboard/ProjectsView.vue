<
<script setup lang="ts">
import * as projectsService from "@/services/projects.service"
import type { IProjects } from "@/interfaces/project.interface"
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
	<PanelTitle v-bind:title="t('MENU.PROJECTS')"></PanelTitle>
	<ItemCard
		class="w-[300px]"
		layout="vertical"
		thumbnail="https://www.gardeners.com/globalassets/articles/gardening/2022content/5062-tomato-seedlings.jpg"
		title="dsadads sad"
		description="dasdasd as da sdasd as da sda dsasd"
		:votes="{ up: 22, down: 2 }"
		:date="new Date()"
	></ItemCard>

	<!-- <Table>
		<TableCaption>A list of your recent projects.</TableCaption>
		<TableHeader>
			<TableRow>
				<TableHead>Name</TableHead>
				<TableHead>Status</TableHead>
				<TableHead>Lauche Date</TableHead>
				<TableHead>Description</TableHead>
				<TableHead>Actions</TableHead>
			</TableRow>
		</TableHeader>
		<TableBody>
			<TableRow v-for="item in projects" :key="item.id">
				<TableCell>
					<span
						@click="
							($event) => {
								console.log($event, item)
							}
						"
						class="w-full h-full cursor-pointer hover:underline hover:text-primary"
						>{{ item.name }}</span
					>
				</TableCell>
				<TableCell>{{ item.is_active }}</TableCell>
				<TableCell>{{ item.launch_date }}</TableCell>
				<TableCell>{{ item.description }}</TableCell>
				<TableCell>
					<DropdownMenu>
						<DropdownMenuTrigger as-child>
							<span
								class="px-2 py-1 bg-border border-[1px] border-primary rounded-md cursor-pointer hover:bg-primary hover:text-primary-foreground"
								><DotsHorizontalIcon
							/></span>
						</DropdownMenuTrigger>
						<DropdownMenuContent class="w-56" align="end">
							<DropdownMenuGroup>
								<DropdownMenuItem>
									<span
										class="w-full h-full flex justify-center items-center"
										@click="
											($event) => {
												console.log($event, item)
											}
										"
										>Edit</span
									>
								</DropdownMenuItem>
							</DropdownMenuGroup>
							<DropdownMenuSeparator />
							<DropdownMenuItem> Delete </DropdownMenuItem>
						</DropdownMenuContent>
					</DropdownMenu>
				</TableCell>
			</TableRow>
		</TableBody>
	</Table> -->
</template>
>
