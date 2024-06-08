<script setup lang="ts">
import * as webinarsService from "@/_services/webinars.service"
import { usePagination } from "@/_libs/usePagination"
import { useRouter, useRoute } from "vue-router"
import type { IWebinars, IResponse } from "@/_interfaces"
// import ItemCard from "@/components/ui/ItemCard.vue"
import PanelTitle from "@/components/layout/menu/PanelTitle.vue"
import FilterComponent from "@/components/layout/filter/Filter.Component.vue"
import PageIntroducerComponent from "@/components/ui/PageIntroducer.Component.vue"
import PaginationComponent from "@/components/layout/pagination/Pagination.Component.vue"
import LoadingDataCardComponent from "@/components/ui/LoadingDataCard.Component.vue"
import ConfirmComponent from "@/components/ui/Confirm.Component.vue"
import ActionTableComponent from "@/components/layout/table/ActionTable.Component.vue"
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
import WebinarsDetailsView from "./WebinarsDetailsView.vue"

onBeforeMount(async () => await fetchData())
const route = useRoute()
const router = useRouter()
const { toast } = useToast()
const { pagination } = usePagination(route)
const { t } = useI18n()
const isLoadingList = ref(false)
const isShowDetailsDialog = ref(false)
const cachedItem = ref<IWebinars | any>(null)
const isConfirmDeleteDialogOpen = ref(false)
const webinars = ref<IWebinars[]>([])
const fetchData = async (page?: number) => {
	isLoadingList.value = true
	if (page) {
		await new Promise((resolve) => setTimeout(resolve, 500000000))
	}
	pagination.page = page || pagination.page
	const response: IResponse<IWebinars[]> | null = (await webinarsService
		.find(pagination)
		.catch((err) => console.error(err))) as IResponse<IWebinars[]>
	isLoadingList.value = false
	if (response?.data) {
		webinars.value = response.data || []
		pagination.total = response.count || 0
	}
}

const onCreateItem = (item?: IWebinars) => {
	if (item) {
		isShowDetailsDialog.value = true
		cachedItem.value = item as IWebinars
	} else router.push(`/dashboard/webinars/details`)
}
const onDeleteItem = (item?: IWebinars) => {
	cachedItem.value = item as IWebinars
	isConfirmDeleteDialogOpen.value = true
}
const onDeleteItemComplete = async () => {
	if (!cachedItem.value) return
	isConfirmDeleteDialogOpen.value = false
	isLoadingList.value = true
	const response = await webinarsService.destroy(cachedItem.value.id).catch(() => {})
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
	{ label: t("WEBINARS.NAME"), value: "name", type: "text" },
	{ label: t("WEBINARS.STATUS"), value: "is_active", type: "badge" },
	{
		label: t("WEBINARS.START_DATE"),
		value: "created_at",
		type: "date"
	},
	{
		label: t("WEBINARS.CREATED_AT"),
		value: "created_at",
		type: "date"
	}
])

const onTableRowAction = (action: string, payload?: IWebinars) => {
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

<template>
	<main class="container flex flex-col sm:gap-4 sm:py-4 sm:pe-14">
		<ConfirmComponent
			action-variant="destructive"
			:action-text="t('GENERAL.ACCEPT')"
			:cancel-text="t('GENERAL.CANCEL')"
			:description="t('GENERAL.ITEM_WILL_BE_DELETED')"
			:title="t('GENERAL.WARN')"
			:is-open="isConfirmDeleteDialogOpen"
			@onaction="() => onDeleteItemComplete()"
			@oncancel="() => (isConfirmDeleteDialogOpen = false)"
		></ConfirmComponent>
		<PanelTitle
			v-bind:title="t('MENU.WEBINARS')"
			:is-breadcrumb="true"
			:breadcrumb-links="[
				{ path: 'webinars', label: t('WEBINARS.PAGE_TITLE') },
				{ path: 'webinars', label: t('WEBINARS.SHOW') }
			]"
		></PanelTitle>
		<FilterComponent
			:items-to-show="ItemsToShow as any"
			:tabs="[
				{ label: t('GENERAL.SHOW_ALL'), name: 'ALL' },
				{ label: t('GENERAL.SHOW_ACTIVE'), name: 'ACTIVE' },
				{ label: t('GENERAL.SHOW_INACTIVE'), name: 'INACTIVE' }
			]"
			:add-title="t('WEBINARS.ADD_NEW')"
			:export-title="t('GENERAL.EXPORT')"
			:filter-title="t('GENERAL.FILTER')"
			:filter-by-title="t('GENERAL.FILTER_BY')"
			@ontabclicked="(tab) => console.log(tab)"
			@on-visibility-changed="(items) => onVisibileITemsChanged(items)"
			@onexport="
				() => {
					console.log('Export Data')
				}
			"
			@onaddnew="
				() => {
					console.log('dsadsad sad Add New')
					onCreateItem()
				}
			"
			@onfilter="(tab) => console.log(tab)"
		></FilterComponent>
		<div
			class="flex flex-row flex-wrap overflow-auto gap-4 items-start sm:mt-4 mt-2"
			v-bind:class="{
				'justify-center': !webinars?.length
			}"
		>
			<div v-if="webinars?.length" class="w-full">
				<Card>
					<CardHeader>
						<CardTitle>{{ t("WEBINARS.PAGE_TITLE") }}</CardTitle>
						<CardDescription>
							{{ t("WEBINARS.SUB_TITLE") }}
						</CardDescription>
					</CardHeader>
					<CardContent
						class="relative"
						v-bind:class="{ 'm-0 p-0 border-0': isLoadingList }"
					>
						<template v-if="isLoadingList">
							<div
								class="w-full h-full z-10 absolute t-0 r-0 l-0 felex justify-center items-center bg-[rgba(255,255,255,0.1)]"
							>
								<LoadingDataCardComponent
									:loading-title="t('GENERAL.LOADING_DATA')"
								></LoadingDataCardComponent>
							</div>
						</template>
						<ActionTableComponent
							:actions="[
								{ action: 'EDIT', label: t('GENERAL.EDIT') },
								{ action: 'DELETE', label: t('GENERAL.DELETE') }
							]"
							:actions-title="t('GENERAL.ACTOINS_TITLE')"
							:images-size="30"
							:icons-size="20"
							:badges-maps="{
								is_active: {
									true: t('GENERAL.SHOW_ACTIVE'),
									false: t('GENERAL.SHOW_INACTIVE')
								}
							}"
							:items="webinars"
							:items-to-show="ItemsToShow as any"
							@on-table-row-action="
								(action, payload) => onTableRowAction(action, payload)
							"
						></ActionTableComponent>
					</CardContent>
					<CardFooter>
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
					</CardFooter>
				</Card>
			</div>
			<div v-else class="w-full">
				<template v-if="isLoadingList">
					<LoadingDataCardComponent
						:loading-title="t('GENERAL.LOADING_DATA')"
					></LoadingDataCardComponent>
				</template>
				<PageIntroducerComponent
					v-else
					:title="t('WEBINARS.ADD_NEW')"
					:description="t('WEBINARS.DESCRIPTION')"
					image="http://localhost:8080/src/assets/images/add-new-item.jpg"
					:add-title="t('WEBINARS.ADD_NEW')"
					@onaddnew="() => onCreateItem()"
				></PageIntroducerComponent>
			</div>
		</div>
		<Dialog
			:default-open="false"
			:open="isShowDetailsDialog"
			@update:open="isShowDetailsDialog = !isShowDetailsDialog"
		>
			<DialogContent class="max-w-screen-xl bg-dashboard">
				<WebinarsDetailsView :default-item="cachedItem"></WebinarsDetailsView>
			</DialogContent>
		</Dialog>
	</main>
</template>
