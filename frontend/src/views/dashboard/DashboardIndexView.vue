<script setup lang="ts">
import { ref } from "vue"
// import { PodcastIcon } from 'lucide-vue-next'
import * as projectsService from "@/services/projects.service"
import DashboardSidebar, {
	type DashboardCategories
} from "@/components/layout/menu/dashboard/DashboardSidebar.vue"
import DashboardMenu from "@/components/layout/menu/dashboard/DashboardMenu.vue"
import { useI18n } from "vue-i18n"
import { onBeforeMount } from "vue"
import type { IPagination, IProjects } from "@/interfaces"

onBeforeMount(async () => {
	const response = await projectsService.find({
		page: 1,
		per_page: 5
	} as IPagination)
	posts.value = response?.data || []
})

const { t } = useI18n()
const posts = ref<IProjects[]>([])
const isCollapsed = ref<boolean>(false)
const categories: DashboardCategories[] = [
	{
		title: t("MENU.DASHBOARD"),
		links: [
			{
				icon: "PieChartIcon",
				label: t("DASHBOARD.SHOW_IT"),
				path: "/dashboard"
			}
		]
	},
	{
		title: "Projects",
		links: [
			{
				icon: "ProjectorIcon",
				label: t("PROJECTS.SHOW"),
				path: "/dashboard/projects"
			},
			{
				icon: "PlusCircleIcon",
				label: t("PROJECTS.ADD_NEW"),
				path: "/dashboard/projects/details"
			}
		]
	},
	{
		title: "Webinars",
		links: [
			{
				icon: "PodcastIcon",
				label: t("WEBINARS.SHOW"),
				path: "/dashboard/webinars"
			},
			{
				icon: "PlusCircleIcon",
				label: t("WEBINARS.ADD_NEW"),
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
		class="w-full min-h-dvh lg:grid lg:grid-cols-[var(--sidebar-width)_1fr] bg-dashboard text-dashboard-foreground"
	>
		<DashboardSidebar
			@ontoggle="ontoggleSidebar()"
			:isCollapsed="isCollapsed"
			:addPostsTitle="t('PROJECTS.ADD_NEW')"
			:posts="posts.map((p) => p.name)"
			:categories="categories"
			:appName="t('APP.NAME')"
		></DashboardSidebar>
		<div class="flex justify-start flex-col items-center min-h-dvh">
			<DashboardMenu :items="[]"></DashboardMenu>
			<router-view></router-view>
		</div>
	</div>
</template>
