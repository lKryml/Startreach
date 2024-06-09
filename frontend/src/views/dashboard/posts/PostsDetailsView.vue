<script setup lang="ts">
import * as yup from "yup"
import * as postsService from "@/_services/posts.service"
import { assignFileFromInput } from "@/_libs/files.utis"
import { useForm } from "vee-validate"

import EditorComponent from "@/components/Editor.Component.vue"
import PanelTitle from "@/components/menu/PanelTitle.vue"
import { Loader2Icon } from "lucide-vue-next"
import { useRoute, useRouter } from "vue-router"
import { useAuthStore } from "@/stores/auth.store"
import { useToast } from "@/shared/shadcn-ui/ui/toast"
import { useI18n } from "vue-i18n"
import type { IPosts } from "@/_interfaces/posts.interface"
import type { IDetailsProps } from "@/_interfaces/global.interface"
import { ref, onBeforeMount } from "vue"
import { Input, Button, Label } from "@/shared/shadcn-ui/ui"
import { watch } from "vue"

const authStore = useAuthStore()
const router = useRouter()
const route = useRoute()
const { defaultItemId, defaultItem } = defineProps<IDetailsProps<IPosts>>()
const emit = defineEmits<{
	(e: "onCreateItem", item: IPosts): void
	(e: "onEditItem", item: IPosts): void
}>()
const content = ref<string>()
const isFormSubmitted = ref(false)

watch(content, (src) => {
	console.log(defaultItem)
})

let itemId: string | number
let currentItem: IPosts = {
	user_id: authStore.currentUser.id,
	profile_id: authStore.currentUser.profile_id
} as IPosts
onBeforeMount(async () => {
	itemId = defaultItemId || (route.params.itemId as string)
	if ((itemId || route.params.itemId) && !defaultItem?.id) {
		const response = await postsService.findById(parseInt(itemId)).catch((e) => console.log(e))
		if (response?.data) {
			currentItem = response?.data as IPosts
			setValues(currentItem)
		} else router.push(`/dashboard/posts`)
	} else if (defaultItem?.id) {
		currentItem = defaultItem || currentItem
		currentItem ? setValues(currentItem) : undefined
	}
})

const authValidatorSchema = yup.object({
	title: yup.string().min(2).required().default(currentItem?.title),
	post: yup.string().min(2).required().default(currentItem?.post),
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
	category_id: yup.number().min(1).optional().default(currentItem?.category_id)
})

const { t } = useI18n()
const { toast } = useToast()
const { errors, defineField, handleSubmit, setValues, values } = useForm({
	validationSchema: authValidatorSchema,
	initialValues: currentItem
})
const [title, titleAttrs] = defineField("title")
const [post, postAttrs] = defineField("post")
const [img64, img64Attrs] = defineField("img64")
const [category, categoryAttrs] = defineField("category_id")
const [tags, tagsAttrs] = defineField("tags")

// const getError = (field: string) => (<any>errors?.value)?.[field]
const onSubmitForm = async (_values: any) => {
	isFormSubmitted.value = true
	const formData = new FormData()
	for (const k in _values) {
		formData.append(k, _values[k])
	}
	const response = await postsService.create(_values).catch(() => {})
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
			itemId = item.id as IPosts["id"]
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
				v-bind:title="t('MENU.POSTS')"
				:is-breadcrumb="true"
				:breadcrumb-links="[
					{ path: 'posts', label: t('POSTS.PAGE_TITLE') },
					{ path: 'posts', label: t('POSTS.ADD_NEW') }
				]"
			></PanelTitle>
			<div class="flex items-start py-10">
				<div
					class="mx-auto grid lg:container lg:w-[800px] md:w-p[650px] sm:w-[450px] w-[350px] gap-6 py-8 rounded-md bg-background border-[1px] border-border"
				>
					<div class="grid gap-2 text-start">
						<h1 class="text-3xl font-bold">{{ t(`POSTS.ADD_TITLE`) }}</h1>
						<p class="text-balance text-muted-foreground">
							{{ t("POSTS.SUB_TITLE") }}
						</p>
					</div>
					<div class="grid grid-col-2 grid-flow-row gap-10 p-5">
						<div class="grid col-span-2 gap-2">
							<Label for="img64">{{ t("POSTS.IMAGE") }}</Label>
							<Input
								@onchange="($event) => onFileChanged($event)"
								class="h-[var(--dashboard-input-height)]"
								v-bind="img64Attrs"
								id="img64"
								type="file"
								:placeholder="t('POSTS.UPLOAD_IMAGE_FOR_POST_BG')"
								v-bind:class="{ 'border-destructive': !!errors.img64 }"
							/>
						</div>
						<div class="grid col-span-2 gap-2">
							<Label for="name">{{ t("POSTS.TITLE") }}</Label>
							<Input
								class="h-[var(--dashboard-input-height)]"
								v-model="title"
								v-bind="titleAttrs"
								id="title"
								type="title"
								placeholder="m@example.com"
								v-bind:class="{ 'border-destructive': !!errors.title }"
							/>
						</div>
						<div class="grid col-span-2 gap-2">
							<Label for="post">{{ t("POSTS.DESCRIPTION") }}</Label>
							<EditorComponent
								@onchange="(content) => (post = content)"
							></EditorComponent>
						</div>
					</div>

					<Button
						type="submit"
						class="h-[var(--dashboard-input-height)] w-full"
						:disabled="isFormSubmitted"
					>
						<template v-if="!isFormSubmitted">{{
							t("POSTS.CREATE_NEW_POST")
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
