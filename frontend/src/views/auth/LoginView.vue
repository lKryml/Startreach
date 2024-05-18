<script setup lang="ts">
import { onBeforeMount } from "vue"
import { useRouter } from "vue-router"
import { Button, Input, Label } from "@/shared/shadcn-ui/ui"
import { useAuthStore } from "@/stores/auth.store"
import { useForm } from "vee-validate"
import * as yup from "yup"

import { useToast } from "@/shared/shadcn-ui/ui/toast"

const authStore = useAuthStore()
const router = useRouter()
const authValidatorSchema = yup.object({
	email: yup.string().email().required(),
	password: yup.string().min(4).required()
})
const { toast } = useToast()
const { errors, defineField, handleSubmit } = useForm({
	validationSchema: authValidatorSchema
})
const [email, emailAttrs] = defineField("email")
const [password, passwordAttrs] = defineField("password")

onBeforeMount(() => {
	authStore.logout()
})
const getError = (field: string) => errors.value?.[field] as string
const onSubmitForm = async (_values: any) => {
	const response = await fetch(`http://127.0.0.1:8000/auth/login`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify(_values)
	}).catch((err) => console.log(err))
	const currentUser = response?.json ? await response.json() : undefined
	if (!currentUser) {
		return toast({
			title: '$t("AUTH.FAILED_LOGIN")',
			description: '$t("AUTH.ENTER_DETAILS")'
		})
	} else {
		console.log(currentUser)
		authStore.login(currentUser)
		router.push("/dashboard")
	}
}
const onSubmitFormErrors = () => {
	console.log(errors.value)
}
const onSubmit = handleSubmit(onSubmitForm, onSubmitFormErrors)
</script>
<template>
	<form
		@submit.prevent="onSubmit"
		class="w-full h-dvh lg:grid lg:min-h-[600px] lg:grid-cols-2 xl:min-h-[800px]"
	>
		<div class="flex items-center justify-center py-12">
			<div class="mx-auto grid w-[350px] gap-6">
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
							<a
								href="/forgot-password"
								class="ml-auto inline-block text-sm underline"
							>
								{{ $t("AUTH.FORGOT_PASSWORD") }}
							</a>
						</div>
						<Input
							v-model="password"
							v-bind="passwordAttrs"
							id="password"
							type="password"
							v-bind:class="{ 'border-destructive': getError('password') }"
							required
						/>
					</div>
					<Button type="submit" class="w-full"> {{ $t("AUTH.LOGIN") }} </Button>
					<Button variant="outline" class="w-full"> Login with Google </Button>
				</div>
				<div class="mt-4 text-center text-sm">
					{{ $t("AUTH.DONT_HAVE_ACCOUNT") }}
					<router-link to="/auth/register" class="underline">
						{{ $t("AUTH.REGISTER") }}
					</router-link>
				</div>
			</div>
		</div>
		<div class="hidden bg-muted lg:block">
			<div class="h-dvh w-full bg-gradient-to-bl from-violet-500 to-blue-500"></div>
		</div>
	</form>
</template>
