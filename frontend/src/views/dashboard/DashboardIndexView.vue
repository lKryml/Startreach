<script setup lang="ts">
import { ref } from "vue"
import DashboardSidebar, {
	type DashboardCategories,
	type DashboardLinks
} from "@/components/layout/menu/dashboard/DashboardSidebar.vue"
import DashboardMenu from "@/components/layout/menu/dashboard/DashboardMenu.vue"
import { menu } from "@/constants/menu/public.menu"
import { cn } from "@/libs/utils"

const isCollapsed = ref<boolean>(false)
const categories: DashboardCategories[] = [
	{
		title: "Projects",
		links: [
			{
				icon: "ProjectorIcon",
				label: "Show Projects",
				path: "/dashboard/projects"
			},
			{
				icon: "PlusCircleIcon",
				label: "Add Project",
				path: "/dashboard/projects/details"
			}
		]
	},
	{
		title: "Webinars",
		links: [
			{
				icon: "ProjectorIcon",
				label: "Show Webinars",
				path: "/dashboard/webinars"
			},
			{
				icon: "PlusCircleIcon",
				label: "Add Webinar",
				path: "/dashboard/webinars/details"
			}
		]
	}
]
const ontoggleSidebar = () => (isCollapsed.value ? onExpand() : onCollapse())
const onCollapse = () => (isCollapsed.value = true)
const onExpand = () => (isCollapsed.value = false)
</script>
<template>
	<div
		class="w-full h-dvh lg:grid lg:min-h-[600px] xl:min-h-[800px] lg:grid-cols-[300px_1fr] bg-dashboard text-dashboard-foreground"
	>
		<DashboardSidebar
			@ontoggle="ontoggleSidebar()"
			:isCollapsed="isCollapsed"
			:posts="['dsad', 'dsadasd ads', 'asdasd asd']"
			:categories="categories"
		></DashboardSidebar>
		<div class="flex justify-start flex-col items-center">
			<DashboardMenu :items="[]"></DashboardMenu>
			<router-view></router-view>
		</div>
	</div>
</template>
