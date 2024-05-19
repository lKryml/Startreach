<script setup lang="ts">
import * as authService from "@/services/auth.service"
import { onBeforeMount, ref } from "vue"
import { useRouter } from "vue-router"
import { Button, Input, Label } from "@/shared/shadcn-ui/ui"
import { useAuthStore } from "@/stores/auth.store"
import { useForm } from "vee-validate"
import * as yup from "yup"

import { useToast } from "@/shared/shadcn-ui/ui/toast"
import { EyeClosedIcon, EyeOpenIcon } from "@radix-icons/vue"

const passwordInputType = ref("password")
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
	const response = await authService.login(_values)
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
		class="w-full h-dvh lg:grid lg:min-h-[600px] xl:min-h-[800px] lg:grid-cols-[350px_1fr]"
	>
		<div class="hidden bg-muted lg:block">
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
							<a
								href="/forgot-password"
								class="ml-auto inline-block text-sm underline"
							>
								{{ $t("AUTH.FORGOT_PASSWORD") }}
							</a>
						</div>
						<Input
							class="h-12"
							v-model="password"
							v-bind="passwordAttrs"
							id="password"
							v-bind:class="{ 'border-destructive': getError('password') }"
							required
							:type="passwordInputType || 'password'"
						/>
						<span v-if="passwordInputType === 'password'"
							><EyeClosedIcon @click="passwordInputType = 'text'"
						/></span>
						<span v-else><EyeOpenIcon @click="passwordInputType = 'password'" /></span>
					</div>
					<Button class="h-12 w-full" type="submit"> {{ $t("AUTH.LOGIN") }} </Button>
					<!-- <Button class="h-12 w-full" variant="outline"> Login with Google </Button> -->
				</div>
				<div class="mt-4 text-center text-sm">
					{{ $t("AUTH.DONT_HAVE_ACCOUNT") }}
					<router-link to="/auth/register" class="underline">
						{{ $t("AUTH.CREATE_NEW_ACCOUNT") }}
					</router-link>
				</div>
			</div>
		</div>
	</form>
</template>
