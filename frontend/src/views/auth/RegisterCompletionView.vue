<script setup lang="ts">
import * as yup from "yup"
import * as authService from "@/services/auth.service"
import { useToast } from "@/shared/shadcn-ui/ui/"
import { Loader2Icon } from "lucide-vue-next"
import EditorComponent from "@/components/layout/editor/Editor.Component.vue"
import ButtonBoxComponent from "@/shared/components/ButtonBoxComponent.vue"
import StepperComponent from "@/shared/components/StepperComponent.vue"
import { Input, Label, Textarea } from "@/shared/shadcn-ui/ui/"
import { useI18n } from "vue-i18n"
import { ref, onBeforeMount } from "vue"
import { useRouter } from "vue-router"
import { useAuthStore } from "@/stores/auth.store"
import { useForm } from "vee-validate"
import { UsersTypesArray } from "@/constants/usersTypes.contant"
import type { IProfile } from "@/interfaces/profiles.interface"

onBeforeMount(() => authStore.logout())

const { t } = useI18n()
const { toast } = useToast()
const authStore = useAuthStore()
const router = useRouter()
const currentStep = ref(1)
const isLoadingData = ref(false)
const authValidatorSchema = yup.object({
	profile_type: yup.number().min(1).max(7).default(1).optional(),
	name: yup.string().min(2).max(150).optional(),
	address: yup.string().min(2).max(300).optional(),
	email: yup.string().email().optional(),
	phone: yup.string().min(9).max(10).optional(),
	bio: yup.string().min(2).max(1500).optional(),
	since: yup.date().optional()
})
const { errors, defineField, handleSubmit } = useForm({
	validationSchema: authValidatorSchema
})
const getError = (field: string) => errors.value?.[field] as string
const [profileType, profileTypeAttrs] = defineField("profile_type")
const [phone, phoneAttrs] = defineField("phone")
const [address, addressAttrs] = defineField("address")
const [email, emailAttrs] = defineField("email")
const [name, nameAttrs] = defineField("name")
const [bio, bioAttrs] = defineField("bio")
const [since, sinceAttrs] = defineField("since")
const onSubmitForm = async (_values: IProfile | any) => {
	const userId = authStore.currentUser?.id
	if (!userId) return
	_values.user_id = userId
	_values.category_id = 1
	isLoadingData.value = true
	const response = await authService.registerCompletion(userId, _values as IProfile)
	const data = response?.json ? await response.json() : undefined
	isLoadingData.value = false
	if (!response?.ok) {
		return toast({
			variant: "destructive",
			title: data.message.startsWith("User already exists")
				? t("AUTH.EMAIL_ALREADY_EXISTS")
				: t("AUTH.FAILED_REGISTER"),
			description: t("AUTH.FAILED_REGISTER_DESCRIPTION")
		})
	} else {
		toast({
			title: t("AUTH.SUCCESS_REGISTER"),
			description: t("AUTH.WILL_BE_ROUTED_TO_HOME")
		})

		authStore.login({
			...authStore.currentUser,
			profile: data.data,
			profile_id: data.data.id
		})
		router.push("/dashboard")
	}
}
const onSubmitFormErrors = () => {}
const onSubmit = handleSubmit(onSubmitForm, onSubmitFormErrors)
</script>
<template>
	<form
		@submit.prevent="onSubmit"
		class="flex justify-center items-center lg:min-h-[600px] xl:min-h-[800px] lg:w-[780px] w-full mx-auto"
	>
		<StepperComponent
			:steps="['profileType', 'info', 'address']"
			:default-step="currentStep"
			:loading="isLoadingData"
			@onnext="(step) => (currentStep = step)"
			@onpreviuos="(step) => (currentStep = step)"
			@onfinish="(step) => {}"
		>
			<div class="flex flex-row gap-2 items-stretch justify-center flex-wrap w-full py-10">
				<ButtonBoxComponent
					v-show="currentStep === 1"
					class="lg:min-w-[160px] xl:min-w-[200px]"
					v-for="(item, index) in UsersTypesArray"
					:key="index"
					:description="t(item.description)"
					:title="t(item.title)"
					:img="item.img"
					:isActive="item.id === profileType"
					@change="profileType = item.id"
				></ButtonBoxComponent>
			</div>
			<div class="flex justify-center items-center px-4 py-12" v-show="currentStep === 2">
				<div class="grid gap-4 grid-cols-2 w-full">
					<div class="grid col-span-2 gap-2">
						<Label for="name">{{ t(`PROFILE.NAME_${profileType || 1}`) }}</Label>
						<Input
							v-model="name"
							v-bind="nameAttrs"
							id="name"
							type="name"
							:placeholder="t(`PROFILE.NAME_${profileType || 1}`)"
							v-bind:class="{ 'border-destructive': getError('name') }"
						/>
					</div>
					<div class="grid gap-2">
						<Label for="phone">{{ t("USERS.PHONE") }}</Label>
						<Input
							v-model="phone"
							v-bind="phoneAttrs"
							id="phone"
							type="phone"
							placeholder="0910000000"
							v-bind:class="{ 'border-destructive': getError('phone') }"
						/>
					</div>
					<div class="grid gap-2">
						<Label for="email">{{ t("USERS.EMAIL") }}</Label>
						<Input
							v-model="email"
							v-bind="emailAttrs"
							id="email"
							type="email"
							placeholder="email@website.net"
							v-bind:class="{ 'border-destructive': getError('email') }"
						/>
					</div>
					<div class="grid col-span-2 gap-2">
						<Label for="address">{{ t("USERS.ADDRESS") }}</Label>
						<Input
							v-model="address"
							v-bind="addressAttrs"
							id="address"
							type="address"
							placeholder="العنوان"
							v-bind:class="{ 'border-destructive': getError('address') }"
						/>
					</div>
				</div>
			</div>

			<div class="flex justify-center items-center px-4 py-12" v-show="currentStep === 3">
				<div class="grid gap-4 grid-cols-2 w-full">
					<!-- <div class="grid col-span-2 gap-2">
						<Label for="name">{{ t(`PROFILE.NAME_${profileType || 1}`) }}</Label>
						<Textarea
							class="w-full h-36"
							v-model="bio"
							v-bind="bioAttrs"
							id="bio"
							type="bio"
							:placeholder="t(`PROFILE.BIO_${profileType || 1}`)"
							v-bind:class="{ 'border-destructive': getError('bio') }"
						></Textarea>
					</div> -->
					<div class="grid col-span-2 gap-2">
						<Label for="description">{{ t(`PROFILE.NAME_${profileType || 1}`) }}</Label>
						<EditorComponent
							@onchange="(content: any) => (bio = content)"
						></EditorComponent>
					</div>
				</div>
			</div>
		</StepperComponent>
	</form>
</template>
