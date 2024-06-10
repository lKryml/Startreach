<script setup lang="ts">
import * as yup from "yup"
import * as webinarsService from "@/_services/webinars.service"
import { datePickerFormat } from "@/_libs/date.utils"
import { assignFileFromInput } from "@/_libs/files.utis"
import { useForm } from "vee-validate"

import EditorComponent from "@/components/Editor.Component.vue"
import PanelTitle from "@/components/menu/PanelTitle.vue"
import { Loader2Icon } from "lucide-vue-next"
import { useRoute, useRouter } from "vue-router"
import { useAuthStore } from "@/stores/auth.store"
import { useToast } from "@/shared/shadcn-ui/ui/toast"
import { useI18n } from "vue-i18n"
import type { IWebinars } from "@/_interfaces/webinars.interface"
import type { IDetailsProps } from "@/_interfaces/global.interface"
import { ref, onBeforeMount } from "vue"
import { Input, Button, Label } from "@/shared/shadcn-ui/ui"
import { watch } from "vue"

const authStore = useAuthStore()
const router = useRouter()
const route = useRoute()
const { defaultItemId, defaultItem } = defineProps<IDetailsProps<IWebinars>>()
const emit = defineEmits<{
	(e: "onCreateItem", item: IWebinars): void
	(e: "onEditItem", item: IWebinars): void
}>()
const content = ref<string>()
const isFormSubmitted = ref(false)

watch(content, (src) => {
	console.log(defaultItem)
})

let itemId: string | number
let currentItem: IWebinars = {
	user_id: authStore.currentUser.id,
	profile_id: authStore.currentUser.profile_id,
	attendees: 0,
	tags: [] as string[],
	description: "",
	name: ""
} as IWebinars
onBeforeMount(async () => {
	itemId = defaultItemId || (route.params.itemId as string)
	if ((itemId || route.params.itemId) && !defaultItem?.id) {
		const response = await webinarsService
			.findById(parseInt(itemId))
			.catch((e) => console.log(e))
		if (response?.data) {
			currentItem = response?.data as IWebinars
			setValues(currentItem)
		} else router.push(`/dashboard/webinars`)
	} else if (defaultItem?.id) {
		currentItem = defaultItem || currentItem
		currentItem ? setValues(currentItem) : undefined
	}
})

const authValidatorSchema = yup.object({
	name: yup.string().min(2).required().default(currentItem?.name),
	description: yup.string().min(2).required().default(currentItem?.description),
	img64: yup.string().min(2).optional().default(currentItem?.img64),
	tags: yup.array().optional().default(currentItem?.tags),
	profile_id: yup
		.number()
		.min(1)
		.required()
		.default(currentItem?.profile_id || authStore.currentUser.profile_id),
	user_id: yup
		.number()
		.min(1)
		.required()
		.default(currentItem?.user_id || authStore.currentUser.id),
	category_id: yup.number().min(1).optional().default(currentItem?.category_id),
	launch_date: yup.date().optional().default(currentItem?.start_date)
})

const { t } = useI18n()
const { toast } = useToast()
const { errors, defineField, handleSubmit, setValues, values } = useForm({
	validationSchema: authValidatorSchema,
	initialValues: currentItem
})
const [name, nameAttrs] = defineField("name")
const [description, descriptionAttrs] = defineField("description")
const [img64, img64Attrs] = defineField("img64")
const [startDate, startDateAttrs] = defineField("start_date")
const [category, categoryAttrs] = defineField("category_id")
const [tags, tagsAttrs] = defineField("tags")

// const getError = (field: string) => (<any>errors?.value)?.[field]
const onSubmitForm = async (_values: any) => {
	isFormSubmitted.value = true
	const formData = new FormData()
	for (const k in _values) {
		formData.append(k, _values[k])
	}
	const response = await webinarsService.create(formData as any).catch(() => {})
	isFormSubmitted.value = false
	const item = response?.data
	if (!item) {
		return toast({
			variant: "destructive",
			title: 't("GENERAL.ERROR")',
			description: 't("GENERAL.EDIT_ITEM_GOES_WRONG")'
		})
	} else {
		if (!itemId) {
			emit("onCreateItem", item)
			itemId = item.id as IWebinars["id"]
		}
		return toast({
			variant: "destructive",
			title: 't("GENERAL.SUCCESS")',
			description: 't("GENERAL.SUCCESSFULLY_EDIT_ITEM")'
		})
	}
}

const onSubmitFormErrors = () => {
	console.log("Error HAppend:", errors.value, values)
}
const onSubmit = handleSubmit(onSubmitForm, onSubmitFormErrors)
const onFileChanged = async ($event: any) => {
	assignFileFromInput({ $event, translator: t, signal: img64, toast, fileType: "image" })
}
</script>
<template>
	<main class="container flex flex-col sm:gap-4 sm:py-4 sm:pe-14">
		<form
			:initial-values="currentItem"
			@submit.prevent="onSubmit"
			class="w-full min-h-full lg:grid"
		>
			<PanelTitle
				v-bind:title="t('MENU.WEBINARS')"
				:is-breadcrumb="true"
				:breadcrumb-links="[
					{ path: 'webinars', label: t('WEBINARS.PAGE_TITLE') },
					{ path: 'webinars', label: t('WEBINARS.ADD_NEW') }
				]"
			></PanelTitle>
			<div class="flex items-start py-10">
				<div
					class="mx-auto grid lg:container lg:w-[800px] md:w-p[650px] sm:w-[450px] w-[350px] gap-6 py-8 rounded-md bg-background border-[1px] border-border"
				>
					<div class="grid gap-2 text-start">
						<h1 class="text-3xl font-bold">{{ t(`WEBINARS.ADD_TITLE`) }}</h1>
						<p class="text-balance text-muted-foreground">
							{{ t("WEBINARS.SUB_TITLE") }}
						</p>
					</div>
					<div class="grid grid-col-2 grid-flow-row gap-10 p-5">
						<div class="grid col-span-2 gap-2">
							<Label for="img64">{{ t("WEBINARS.IMAGE") }}</Label>
							<Input
								@onchange="($event) => onFileChanged($event)"
								class="h-[var(--dashboard-input-height)]"
								v-bind="img64Attrs"
								id="img64"
								type="file"
								:placeholder="t('WEBINARS.UPLOAD_IMAGE_FOR_PROJECT_BG')"
								v-bind:class="{ 'border-destructive': !!errors.name }"
							/>
						</div>
						<div class="grid col-span-2 gap-2">
							<Label for="name">{{ t("WEBINARS.NAME") }}</Label>
							<Input
								class="h-[var(--dashboard-input-height)]"
								v-model="name"
								v-bind="nameAttrs"
								id="name"
								type="name"
								placeholder="m@example.com"
								v-bind:class="{ 'border-destructive': !!errors.name }"
							/>
						</div>
						<div class="grid gap-2">
							<Label for="date" class="shrink-0"
								>{{ t("WEBINARS.START_DATE") }}
							</Label>
							<VueDatePicker
								:format="datePickerFormat"
								v-model="startDate"
								@date-update="(date: Date) => setValues({ start_date: date })"
							/>
						</div>
						<div class="grid col-span-2 gap-2">
							<Label for="description">{{ t("WEBINARS.DESCRIPTION") }}</Label>
							<EditorComponent
								@onchange="(content) => (description = content)"
							></EditorComponent>
						</div>
					</div>

					<Button
						type="submit"
						class="h-[var(--dashboard-input-height)] w-full"
						:disabled="isFormSubmitted"
					>
						<template v-if="!isFormSubmitted">{{
							t("WEBINARS.CREATE_NEW_PROJECT")
						}}</template>
						<template v-else>
							<Loader2Icon class="w-8 h-8 me-2 animate-spin" />
							{{ t("GENERAL.WAIT_SUBMITTING_DATA") }}
						</template>
					</Button>
				</div>
			</div>
		</form>
	</main>
</template>
