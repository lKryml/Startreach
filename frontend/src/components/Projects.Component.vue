
<template>
    <section id="hero" class="bg-[url('/images/projects-hero.png')] bg-no-repeat backy w-full">
		<div
			class=" h-dvh gap-0 w-full justify-center items-center   mb-0"
		>
			<div
				class="flex-1 flex-col h-full flex justify-center items-end bg-transparent px-10 md:px-40 mb-0   mt-16"
			>
				<div class="pb-8 w-full">
					<div
						class="text-8xl font-extrabold flex items-start flex-col gap-5  text-center"
					>
						<span class="w-full drop-shadow-lg">We invest in people who are</span>
						<span class="w-full drop-shadow-lg text-7xl"> Always Passionate</span>
						<span class="w-full drop-shadow-lg text-5xl ">about what they do</span>
					</div>
				</div>
				<div class=" w-full  flex flex-col justify-center text-center gap-10">
					<h3 class="top-startups text-4xl drop-shadow-xl pb-8">See our top Startups</h3>
					<img class="mx-auto h-2/4 pb-10 " src="/images/strarrow.png">
				</div>
				<div class="w-full flex flex-col ">
			<div class="w-full flex justify-center align-center gap-28 text-2xl font-bold drop-shadow-2xl pb-16 ">
				
				<a :class="{ 'target:font-extrabolde': filter === 'all' }">All</a>
            <a :class="{ 'target:font-extrabolde': filter === 'trending' }">Trending Startups</a>
            <a :class="{ 'target:font-extrabolde': filter === 'top' }">Top Startups</a>
            <a :class="{ 'target:font-extrabolde': filter === 'latest' }">Latest Startups</a></div>
			</div>
			
			</div>
			<div class="projects-section  justify-items-center bg-[url('/images/projects-hero22.png')] bg-no-repeat backy2">
  <div class="project-card" v-for="project in projects" :key="project.id">
    <div class="project-thumbnail">
      <img :src=project.img alt="Project 1 thumbnail">
    </div>
    <h2 class="font-extrabold text-3xl">{{project.name}}</h2>
    
    <p>{{project.description}}</p>
    <button class="details-btn">View Details</button>
  </div>
  <div class="project-card">
    <div class="project-thumbnail">
      <img src="/images/hd.jpg" alt="Project 2 thumbnail">
    </div>
    <h2>Project Title 2</h2>
    <p class="subheading">Project Subheading 2</p>
    <p>Project details go here. Lorem ipsum dolor sit amet...</p>
    <button class="details-btn">View Details</button>
  </div>
  <div class="project-card">
    <div class="project-thumbnail">
      <img src="/images/hd.jpg" alt="Project 3 thumbnail">
    </div>
    <h2>Project Title 3</h2>
    <p class="subheading">Project Subheading 3</p>
    <p>Project details go here. Lorem ipsum dolor sit amet...</p>
    <button class="details-btn">View Details</button>
  </div>
  <div class="project-card">
    <div class="project-thumbnail">
      <img src="/images/hd.jpg" alt="Project 4 thumbnail">
    </div>
    <h2>Project Title 4</h2>
    <p class="subheading ">Project Subheading 4</p>
    <p>Project details go here. Lorem ipsum dolor sit amet...</p>
    <button class="details-btn">View Details</button>
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
							<!-- Showing <strong>1-10</strong> of <strong>32</strong>
							products -->
						</div>
	</section>
  
</template>
<style scoped>
.backy{
	background-size: cover;
	background-position: 75% 0%;
}
.backy2{
	background-size: cover;
	background-position: 75% 50%;
}

.top-startups{
	color:rgb(254, 145, 104);
}
.drop-shadow-xl {
    filter: drop-shadow(0 5px 10px rgba(254, 145, 104,0.40)); /* Red color with opacity */
  }

.projects-section {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* Defines two columns of equal width */
  grid-gap: 20px; /* Optional spacing between project cards */
  
}

.project-card {
	margin-top: 20px;
  width: 625px;
  height: 575px;
  background-color: transparent;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  padding: 20px; /* Adds padding for content */
}
.target:font-extrabolde {
  font-weight: extrabold; /* Style the active link to be bolder */
  color: rgb(104, 254, 111) !important; /* Optional: Change link color for better distinction */
}







.project-thumbnail {
	border-radius: 3px;
	cursor: pointer;
  width: 100%; /* Stretches to full card width */
  height: 325px; /* Adjust height as needed */
  margin-bottom: 10px; /* Adds spacing below the image */
  overflow: hidden; /* Ensures image doesn't overflow container */
}

.project-thumbnail img {
  width: 100%; /* Stretches image to fit container */
  height: 100%; /* Stretches image to fit container */
  object-fit: cover; /* Scales image to cover the container */
}
</style>
<script setup lang="ts">
let filter: string = 'all';
import * as projectsService from "@/_services/projects.service"
import { usePagination } from "@/_libs/usePagination"
import { useRouter, useRoute } from "vue-router"
import type { IProjects, IResponse } from "@/_interfaces"
// import ItemCard from "@/components/ui/ItemCard.vue"
import PanelTitle from "@/components/menu/PanelTitle.vue"
import FilterComponent from "@/components/Filter.Component.vue"
import PageIntroducerComponent from "@/components/ui/PageIntroducer.Component.vue"
import PaginationComponent from "@/components/Pagination.Component.vue"
import LoadingDataCardComponent from "@/components/ui/LoadingDataCard.Component.vue"
import ConfirmComponent from "@/components/ui/Confirm.Component.vue"
import ActionTableComponent from "@/components/ActionTable.Component.vue"
import { useI18n } from "vue-i18n"
import { onBeforeMount } from "vue"
import { ref } from "vue"
import { useToast } from "@/shared/shadcn-ui/ui"
import {
	Card,
	CardContent,
	CardDescription,
	CardFooter,
	CardHeader,
	CardTitle
} from "@/shared/shadcn-ui/ui/card"
import { Dialog, DialogContent } from "@/shared/shadcn-ui/ui"
import ProjectsDetailsView from "../projects/ProjectsDetailsView.vue"

onBeforeMount(async () => await fetchData())
const route = useRoute()
const router = useRouter()
const { toast } = useToast()
const { pagination } = usePagination(route)
const { t } = useI18n()
const isLoadingList = ref(false)
const isShowDetailsDialog = ref(false)
const cachedItem = ref<IProjects | any>(null)
const isConfirmDeleteDialogOpen = ref(false)
const projects = ref<IProjects[]>([])
const fetchData = async (page?: number) => {
	isLoadingList.value = true
	if (page) {
		await new Promise((resolve) => setTimeout(resolve, 500000000))
	}
	pagination.page = page || pagination.page
	const response: IResponse<IProjects[]> | null = (await projectsService
		.find(pagination)
		.catch((err) => console.error(err))) as IResponse<IProjects[]>
	isLoadingList.value = false
	if (response?.data) {
		projects.value = response.data || []
		pagination.total = response.count || 0
	}
}

const onCreateItem = (item?: IProjects) => {
	if (item) {
		isShowDetailsDialog.value = true
		cachedItem.value = item as IProjects
	} else router.push(`/dashboard/projects/details`)
}
const onDeleteItem = (item?: IProjects) => {
	cachedItem.value = item as IProjects
	isConfirmDeleteDialogOpen.value = true
}
const onDeleteItemComplete = async () => {
	if (!cachedItem.value) return
	isConfirmDeleteDialogOpen.value = false
	isLoadingList.value = true
	const response = await projectsService.destroy(cachedItem.value.id).catch(() => {})
	console.log(response)
	if (!response) {
		isLoadingList.value = false
		return toast({
			variant: "destructive",
			title: t("GENERAL.ERROR"),
			description: t("GENERAL.FAIL_DELETE_ITEM"),
			duration: 5000
		})
	}
	await fetchData()
	isLoadingList.value = false
}

const ItemsToShow = ref([
	{ label: t("PROJECTS.NAME"), value: "name", type: "text" },
	{ label: t("PROJECTS.STATUS"), value: "is_active", type: "badge" },
	{
		label: t("PROJECTS.LUNCHED_DATE"),
		value: "created_at",
		type: "date"
	},
	{
		label: t("PROJECTS.CREATED_AT"),
		value: "created_at",
		type: "date"
	}
])

const onTableRowAction = (action: string, payload?: IProjects) => {
	switch (action) {
		case "EDIT":
			return onCreateItem(payload)
		case "DELETE":
			return onDeleteItem(payload)
		default:
			break
	}
}
const onVisibileITemsChanged = (items: any) => {
	return (ItemsToShow.value = items as any)
}
</script>