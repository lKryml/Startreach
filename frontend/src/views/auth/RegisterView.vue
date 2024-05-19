<script setup lang="ts">
import * as authService from "@/services/auth.service"
import { onBeforeMount } from "vue"
import { useRouter } from "vue-router"
import { Button, Input, Label } from "@/shared/shadcn-ui/ui"
import { useAuthStore } from "@/stores/auth.store"
import { useForm } from "vee-validate"
import { useI18n } from "vue-i18n"
import * as yup from "yup"

import { useToast } from "@/shared/shadcn-ui/ui/toast"

const { t } = useI18n()
const authStore = useAuthStore()
const router = useRouter()
const authValidatorSchema = yup.object({
	user_type: yup.number().min(1).max(7).default(1)
})
const { toast } = useToast()
const { errors, defineField, handleSubmit } = useForm({
	validationSchema: authValidatorSchema
})
const [email, emailAttrs] = defineField("email")
const [password, passwordAttrs] = defineField("password")
const [confirmPassword, confirmPasswordAttrs] = defineField("confirm_password")

onBeforeMount(() => {
	authStore.logout()
})
const getError = (field: string) => errors.value?.[field] as string
const onSubmitForm = async (_values: any) => {
	const response = await authService.register(_values)
	const data = response?.json ? await response.json() : undefined
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
		authStore.login(data)
		router.push("/dashboard")
	}
}
const onSubmitFormErrors = () => {}
const onSubmit = handleSubmit(onSubmitForm, onSubmitFormErrors)
</script>
<template>
	<form
		@submit.prevent="onSubmit"
		class="w-full h-dvh lg:grid lg:min-h-[600px] xl:min-h-[800px] lg:grid-cols-[350px_1fr]"
	>
		<div
			class="hidden bg-muted lg:block bg-[url('https://cdn.dribbble.com/userupload/12700543/file/original-2f761db0abe85c110884800f36395c9e.png?resize=1600x1200')] bg-[center_-283px]"
		>
			<div
				class="h-dvh w-full bg-gradient-to-bl from-violet-500 to-blue-500 bg-[url('https://cdn.dribbble.com/userupload/12700543/file/original-2f761db0abe85c110884800f36395c9e.png?resize=1600x1200')] bg-[center_-283px]"
			></div>
		</div>
		<div class="flex items-center justify-center py-12">
			<div class="mx-auto grid sm:w-[450px] w-[350px] gap-6">
				<div class="grid gap-2 text-center">
					<h1 class="text-3xl font-bold">{{ $t("AUTH.LOGIN") }}</h1>
					<p class="text-balance text-muted-foreground">
						{{ $t("AUTH.ENTER_DETAILS") }}
					</p>
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
					<Button type="submit" class="h-12 w-full">
						{{ $t("AUTH.CREATE_NEW_ACCOUNT") }}
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
