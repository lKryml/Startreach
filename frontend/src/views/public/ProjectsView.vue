<script setup lang="ts">
import * as projectsService from "@/_services/projects.service"
import { usePagination } from "@/_libs/usePagination"
import { useRoute } from "vue-router"
import type { IProjects, IResponse } from "@/_interfaces"
import PaginationComponent from "@/components/Pagination.Component.vue"
import { useI18n } from "vue-i18n"
import { onBeforeMount } from "vue"
import { ref } from "vue"
import { useToast, Button } from "@/shared/shadcn-ui/ui"
import { Loader2Icon } from "lucide-vue-next"
import { useAuthStore } from "@/stores/auth.store"
import router from "@/router"

const filter = ref<string>("all")
const authStore = useAuthStore()
onBeforeMount(async () => await fetchData())
const route = useRoute()
const { t } = useI18n()

const { pagination } = usePagination(route)
const isLoadingList = ref(false)

const projects = ref<IProjects[]>([])
const fetchData = async (page?: number) => {
	isLoadingList.value = true
	pagination.page = page || pagination.page
	pagination.sort = "desc"
	const response: IResponse<IProjects[]> | null = (await projectsService
		.find(pagination)
		.catch((err) => console.error(err))) as IResponse<IProjects[]>
	isLoadingList.value = false
	if (response?.data) {
		projects.value = response.data || []
		pagination.total = response.count || 0
	}
}

const onInvestProject = (event: MouseEvent, project: IProjects) => {
	event.preventDefault()
	if (authStore.isAuth) {
		router.push("/auth/login")
	}
	console.log("Investing in project", project.name)
}
</script>

<template>
	<section id="hero" class="backy w-full">
		<div class="w-full justify-center items-center mb-0">
			<div
				class="flex-1 flex-col flex justify-center items-end bg-transparent px-10 md:px-40 mb-0 mt-16 h-dvh bg-[url('/images/projects-hero.png')] bg-no-repeat bg-cover"
			>
				<div class="pb-8 w-full">
					<div
						class="text-8xl font-extrabold flex items-start flex-col gap-5 text-center"
					>
						<span class="w-full drop-shadow-lg">We invest in people who are</span>
						<span class="w-full drop-shadow-lg text-7xl"> Always Passionate</span>
						<span class="w-full drop-shadow-lg text-5xl">about what they do</span>
					</div>
				</div>
				<div class="w-full flex flex-col justify-center text-center gap-10">
					<h3 class="text-[#fe9168] text-4xl drop-shadow-xl pb-8">
						See our top Startups
					</h3>
					<img class="mx-auto h-2/4 pb-10" src="/images/strarrow.png" />
				</div>
			</div>

			<div
				class="w-full flex justify-center items-center p-16 bg-gradient-to-t from-background to-transparent"
			>
				<div
					class="w-full flex justify-center align-center gap-28 text-2xl font-bold drop-shadow-2xl"
				>
					<a
						class="cursor-pointer"
						:class="{ 'text-primary': filter === 'all' }"
						@click="filter = 'all'"
						>All</a
					>
					<a
						class="cursor-pointer"
						:class="{ 'text-primary': filter === 'trending' }"
						@click="filter = 'trending'"
						>Trending Startups</a
					>
					<a
						class="cursor-pointer"
						:class="{ 'text-primary': filter === 'top' }"
						@click="filter = 'top'"
						>Top Startups</a
					>
					<a
						class="cursor-pointer"
						:class="{ 'text-primary': filter === 'latest' }"
						@click="filter = 'latest'"
						>Latest Startups</a
					>
				</div>
			</div>

			<div class="projects-section flex justify-items-center py-20">
				<div class="container grid gap-5 xl:grid-cols-2 md:grid-cols-2 grid-cols-1">
					<template v-if="!isLoadingList && projects?.length">
						<div
							class="project-card mt-5 w-full h-[550px] rounded-lg bg-transparent border-[1px] border-border p-5 hover:shadow-xl hover:border-primary hover:cursor-pointer"
							v-for="project in projects"
							:key="project.id"
						>
							<div class="flex flex-col justify-start h-full">
								<div class="flex justify-start flex-1 flex-col">
									<div
										class="project-thumbnail h-[325px] cursor-pointer w-full mb-4 overflow-hidden rounded"
									>
										<img
											class="w-full h-full object-cover"
											:src="project.img || '/images/hd.jpg'"
											:alt="project.name"
										/>
									</div>
									<h2 class="font-extrabold text-3xl py-2">
										{{ project.name }}
									</h2>
									<h3
										class="pb-2 max-h-[52px] text-ellipsis text-wrap overflow-hidden"
									>
										{{ project.description }}
									</h3>
								</div>
								<div class="h-12 flex">
									<router-link :to="`/projects/${project.id}`">
										<Button variant="secondary" class="me-1"
											>View Details</Button
										>
									</router-link>
									<Button
										@click="onInvestProject($event, project)"
										variant="outline"
										>Invest</Button
									>
								</div>
							</div>
						</div>
					</template>
					<template v-else>
						<div class="flex justify-center items-center h-dvh w-full">
							<Loader2Icon class="w-20 h-20 me-2 animate-spin" />
						</div>
					</template>
				</div>
			</div>
		</div>
		<div class="text-xs text-muted-foreground">
			<PaginationComponent
				:disabled="isLoadingList"
				:items-perpage="pagination.per_page"
				:total="pagination.total"
				:current-page="pagination.page"
				@onpagechanged="(page: number) => fetchData(page)"
			></PaginationComponent>
		</div>
	</section>
</template>
