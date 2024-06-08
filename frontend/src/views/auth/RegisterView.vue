<script setup lang="ts">
import * as authService from "@/_services/auth.service"
import { onBeforeMount, ref } from "vue"
import { useRouter } from "vue-router"
import { Loader2Icon } from "lucide-vue-next"
import { Button, Input, Label } from "@/shared/shadcn-ui/ui"
import { useAuthStore } from "@/stores/auth.store"
import { useForm } from "vee-validate"
import { useI18n } from "vue-i18n"
import * as yup from "yup"

import { useToast } from "@/shared/shadcn-ui/ui/toast"

const { t } = useI18n()
const authStore = useAuthStore()
const router = useRouter()
const isLoadingData = ref(false)
const authValidatorSchema = yup.object({
	first_name: yup.string().required(),
	last_name: yup.string().required(),
	email: yup.string().required().email(),
	password: yup.string().required().min(4),
	confirm_password: yup
		.string()
		.required()
		.min(4)
		.oneOf([yup.ref("password")])
})
const { toast } = useToast()
const { errors, defineField, handleSubmit } = useForm({
	validationSchema: authValidatorSchema
})
const [firstName, firstNameAttrs] = defineField("first_name")
const [lastName, lastNameAttrs] = defineField("last_name")
const [email, emailAttrs] = defineField("email")
const [password, passwordAttrs] = defineField("password")
const [confirmPassword, confirmPasswordAttrs] = defineField("confirm_password")

onBeforeMount(() => {
	if (authStore.isAuth) {
		router.push(
			`${authStore.currentUser?.profile_id ? "/dashboard" : "/auth/register-completion"}`
		)
	}
})
const getError = (field: string) => errors.value?.[field] as string
const onSubmitForm = async (_values: any) => {
	isLoadingData.value = true
	const response = await authService.register(_values)
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
		authStore.login(data.data)
		router.push("/auth/register-completion")
	}
}
const onSubmitFormErrors = () => {}
const onSubmit = handleSubmit(onSubmitForm, onSubmitFormErrors)
</script>
<template>
	<form @submit.prevent="onSubmit" class="w-full h-dvh lg:grid lg:min-h-[600px] xl:min-h-[800px]">
		<div class="flex items-center justify-center py-12">
			<div class="mx-auto grid sm:w-[450px] w-[350px] gap-6">
				<div class="grid gap-2 text-center">
					<h1 class="text-3xl font-bold">{{ $t("AUTH.LOGIN") }}</h1>
					<p class="text-balance text-muted-foreground">
						{{ $t("AUTH.ENTER_DETAILS") }}
					</p>
				</div>

				<div class="grid grid-col-2 grid-flow-col gap-4">
					<div class="grid gap-2">
						<Label for="firstName">{{ $t("USERS.FIRST_NAME") }}</Label>
						<Input
							class="h-12"
							v-model="firstName"
							v-bind="firstNameAttrs"
							id="firstName"
							type="firstName"
							:placeholder="$t('USERS.FIRST_NAME')"
							v-bind:class="{ 'border-destructive': getError('firstName') }"
						/>
					</div>
					<div class="grid gap-2">
						<Label for="lastName">{{ $t("USERS.LAST_NAME") }}</Label>
						<Input
							class="h-12"
							v-model="lastName"
							v-bind="lastNameAttrs"
							id="lastName"
							type="lastName"
							:placeholder="$t('USERS.LAST_NAME')"
							v-bind:class="{ 'border-destructive': getError('lastName') }"
						/>
					</div>
				</div>
				<div class="grid gap-4">
					<div class="grid gap-2">
						<Label for="email">{{ $t("USERS.EMAIL") }}</Label>
						<Input
							class="h-12"
							v-model="email"
							v-bind="emailAttrs"
							id="email"
							type="email"
							placeholder="m@example.com"
							v-bind:class="{ 'border-destructive': getError('email') }"
						/>
					</div>
					<div class="grid gap-2">
						<div class="flex items-center">
							<Label for="password">{{ $t("USERS.PASSWORD") }}</Label>
						</div>
						<Input
							class="h-12"
							v-model="password"
							v-bind="passwordAttrs"
							id="password"
							type="password"
							v-bind:class="{ 'border-destructive': getError('password') }"
							required
						/>
					</div>
					<div class="grid gap-2">
						<div class="flex items-center">
							<Label for="confirmPassword">{{ $t("USERS.CONFIRM_PASSWORD") }}</Label>
						</div>
						<Input
							class="h-12"
							v-model="confirmPassword"
							v-bind="confirmPasswordAttrs"
							id="confirmPassword"
							type="password"
							v-bind:class="{ 'border-destructive': getError('confirmPassword') }"
							required
						/>
					</div>
					<Button class="h-12 w-full" type="submit" :disabled="isLoadingData">
						<span class="w-full h-full m-0 p-0" v-if="!isLoadingData">{{
							$t("AUTH.CREATE_NEW_ACCOUNT")
						}}</span>
						<Loader2Icon v-else class="w-8 h-8 me-2 animate-spin" />
					</Button>
					<!-- <Button variant="outline" class="h-12 w-full"> Signup with Google </Button> -->
				</div>

				<div class="mt-4 text-center text-sm">
					{{ $t("AUTH.HAV_ACCOUNT") }} ...
					<router-link to="/auth/login" class="underline">
						{{ $t("AUTH.LOGIN") }}
					</router-link>
				</div>
			</div>
		</div>
	</form>
</template>
