<script setup lang="ts">
import { enviroment } from "@/enviroments/enviroment"
import * as projectsService from "@/_services/projects.service"
import { useRoute, useRouter } from "vue-router"
import { useI18n } from "vue-i18n"
import { ref, onBeforeMount } from "vue"
import { Button } from "@/shared/shadcn-ui/ui"
import type { IProjects, IResponse } from "@/_interfaces"

const route = useRoute()
const router = useRouter()
const itemId = parseInt(route.params.itemId as string)
const { t } = useI18n()
onBeforeMount(async () => await fetchData())
const isLoadingList = ref(false)

const project = ref<IProjects>()
const fetchData = async (page?: number) => {
	isLoadingList.value = true
	const response: IResponse<IProjects> | null = (await projectsService
		.findById(itemId)
		.catch((err) => console.error(err))) as IResponse<IProjects>
	isLoadingList.value = false
	if (response?.data) {
		project.value = response.data || []
	} else {
		router.push("/404")
	}
}
</script>

<template>
	<section id="hero" class="backy w-full">
		<div class="w-full justify-center items-center mb-0">
			<div
				class="bg-gradient-to-br from-primary to-secondary flex-1 flex-col flex justify-center items-end bg-transparent px-10 md:px-40 mb-0 mt-16 h-dvh bg-no-repeat bg-cover"
				:style="`background-image: url(${enviroment.baseUrl}/images/${project?.img || ''})`"
			></div>
		</div>
		<div class="w-full">
			<div
				class="container flex justify-center items-center py-20"
				v-html="project?.description"
			></div>
		</div>
	</section>
</template>
