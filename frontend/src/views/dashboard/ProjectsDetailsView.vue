<script setup lang="ts">
import * as yup from "yup"
import * as projectsService from "@/services/projects.service"
import { useForm } from "vee-validate"

import DatePicker from "@/components/ui/DatePicker.component.vue"
import { useRouter } from "vue-router"
import { useAuthStore } from "@/stores/auth.store"
import { useToast } from "@/shared/shadcn-ui/ui/toast"
import { useI18n } from "vue-i18n"
import type { IProjects } from "@/interfaces/project.interface"
import type { IDetailsProps } from "@/interfaces/global.interface"
import { onBeforeMount } from "vue"
import { Textarea, Input, Switch, Button, Label } from "@/shared/shadcn-ui/ui"

const authStore = useAuthStore()
const router = useRouter()
const { itemId, defaultItem } = defineProps<IDetailsProps<IProjects>>()

let currentItem: IProjects = {
	user_id: authStore.currentUser.id,
	profile_id: authStore.currentUser.profile_id,
	category_id: 1,
	launch_date: new Date()
} as IProjects
onBeforeMount(async () => {
	if (itemId && !defaultItem?.id) {
		const response: any = await projectsService
			.findById(parseInt(itemId))
			.catch((e) => console.log(e))
		if (response?.ok) {
			currentItem = response.json ? await response.json() : undefined
		} else router.push(`/dashboard/projects`)
	} else if (defaultItem?.id) currentItem = defaultItem || currentItem
})

const authValidatorSchema = yup.object({
	name: yup.string().min(2).required().default(currentItem?.name),
	description: yup.string().min(2).required().default(currentItem?.description),
	img: yup.string().min(2).optional().default(currentItem?.img),
	tags: yup.array().optional().default(currentItem?.tags),
	employees_count: yup.number().optional().default(currentItem?.employees_count),
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
	launch_date: yup.date().optional().default(currentItem?.launch_date),
	is_launched: yup.boolean().optional().default(!!currentItem?.launch_date),
	need_investores: yup.boolean().optional().default(currentItem?.need_investores)
})

const { t } = useI18n()
const { toast } = useToast()
const { errors, defineField, handleSubmit, setValues, values } = useForm({
	validationSchema: authValidatorSchema,
	initialValues: currentItem
})
const [name, nameAttrs] = defineField("name")
const [description, descriptionAttrs] = defineField("description")
const [launchDate, launchDateAttrs] = defineField("launch_date")
const [isLaunched, isLaunchedAttrs] = defineField("is_launched")
const [category, categoryAttrs] = defineField("category_id")
const [img, imgAttrs] = defineField("img")
const [tags, tagsAttrs] = defineField("tags")
const [needInvestores, needInvestoresAttrs] = defineField("need_investores")

// const getError = (field: string) => (<any>errors?.value)?.[field]
const onSubmitForm = async (_values: any) => {
	const response = await projectsService.create(_values).catch((e) => {})
	const item = (response?.json ? await response.json() : undefined)?.data
	if (!item) {
		return toast({
			title: 't("AUTH.FAILED_LOGIN")',
			description: 't("AUTH.ENTER_DETAILS")'
		})
	} else {
		console.log(item)
	}
}
const onSubmitFormErrors = () => {
	console.log("Error HAppend:", errors.value)
}
const onSubmit = handleSubmit(onSubmitForm, onSubmitFormErrors)
</script>
<template>
	<form
		:initial-values="currentItem"
		@submit.prevent="onSubmit"
		class="w-full h-dvh lg:grid lg:min-h-[600px] xl:min-h-[800px]"
	>
		<div class="flex items-start py-12">
			<div
				class="mx-auto grid lg:container lg:w-[800px] md:w-p[650px] sm:w-[450px] w-[350px] gap-6 py-8 rounded-md bg-background border-[1px] border-border"
			>
				<div class="grid gap-2 text-start">
					<h1 class="text-3xl font-bold">{{ t(`PROJECTS.PAGE_TITLE`) }}</h1>
					<p class="text-balance text-muted-foreground">
						{{ t("PROJECTS.ENTER_DETAILS") }}
					</p>
				</div>
				<div class="grid grid-col-2 grid-flow-row gap-10 p-5">
					<div class="grid col-span-2 gap-2">
						<Label for="name">{{ $t("PROJECTS.NAME") }}</Label>
						<Input
							class="h-12"
							v-model="name"
							v-bind="nameAttrs"
							id="name"
							type="name"
							placeholder="m@example.com"
							v-bind:class="{ 'border-destructive': !!errors.name }"
						/>
					</div>
					<!-- <div class="w-full">
						<Switch id="is-launched" v-mode="isLaunched" v-bind="isLaunchedAttrs" />
						<Label for="is-launched">{{ t("PROJECTS.IS_LAUNCHED") }}</Label>
					</div> -->
					<div class="grid gap-2">
						<Label for="date" class="shrink-0">{{ t("PROJECTS.LAUNCHE_DATE") }} </Label>
						<DatePicker
							@ondatechanged="
								(date) => {
									setValues({ ...values, launch_date: date })
								}
							"
							class="w-full h-12"
						/>
					</div>
					<div class="grid col-span-2 gap-2">
						<Label for="description">{{ $t("PROJECTS.DESCRIPTION") }}</Label>
						<Textarea
							class="h-12"
							v-model="description"
							v-bind="descriptionAttrs"
							id="description"
							type="description"
							placeholder="m@example.com"
							v-bind:class="{ 'border-destructive': errors.description }"
						></Textarea>
					</div>
				</div>

				<Button type="submit" class="h-12 w-full">
					{{ $t("AUTH.CREATE_NEW_ACCOUNT") }}
				</Button>
			</div>
		</div>
	</form>
</template>
