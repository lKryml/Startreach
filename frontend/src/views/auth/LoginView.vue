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
import { EyeClosedIcon, EyeOpenIcon } from "@radix-icons/vue"

const authStore = useAuthStore()
const passwordInputType = ref("password")
const isLoadingData = ref(false)
const router = useRouter()
const authValidatorSchema = yup.object({
	email: yup.string().email().required(),
	password: yup.string().min(4).required()
})
const { t } = useI18n()
const { toast } = useToast()
const { errors, defineField, handleSubmit } = useForm({
	validationSchema: authValidatorSchema
})
const [email, emailAttrs] = defineField("email")
const [password, passwordAttrs] = defineField("password")

onBeforeMount(() => authStore.logout())

const getError = (field: string) => errors.value?.[field] as string
const onSubmitForm = async (_values: any) => {
	isLoadingData.value = true
	const response = await authService.login(_values)
	const currentUser = (response?.json ? await response.json() : undefined)?.data
	isLoadingData.value = false
	if (!currentUser) {
		return toast({
			title: t("AUTH.FAILED_LOGIN"),
			description: t("AUTH.ENTER_DETAILS")
		})
	} else {
		authStore.login(currentUser)
		if (currentUser.profile_id) router.push("/dashboard")
		else router.push("/auth/register-completion")
	}
}
const onSubmitFormErrors = () => {
	console.log("Error HAppend:", errors.value)
}
const onSubmit = handleSubmit(onSubmitForm, onSubmitFormErrors)
</script>
<template>
	<form
		@submit.prevent="onSubmit"
		class="w-full h-full lg:grid lg:min-h-[600px] xl:min-h-[800px]"
	>
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
							class="h-[var(--dashboard-input-height)]"
							v-model="email"
							v-bind="emailAttrs"
							id="email"
							type="email"
							placeholder="m@example.com"
							v-bind:class="{ 'border-destructive': getError('email') }"
						/>
					</div>
					<div class="grid gap-2 relative">
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
							class="h-[var(--dashboard-input-height)]"
							v-model="password"
							v-bind="passwordAttrs"
							id="password"
							v-bind:class="{ 'border-destructive': getError('password') }"
							required
							:type="passwordInputType || 'password'"
						/>
						<span
							class="absolute cursor-pointer top-10 end-4"
							v-if="passwordInputType === 'password'"
							><EyeClosedIcon @click="passwordInputType = 'text'"
						/></span>
						<span class="absolute cursor-pointer top-10 end-4" v-else
							><EyeOpenIcon @click="passwordInputType = 'password'"
						/></span>
					</div>
					<Button
						class="h-[var(--dashboard-input-height)] w-full"
						type="submit"
						:disabled="isLoadingData"
					>
						<span class="w-full h-full m-0 p-0" v-if="!isLoadingData">{{
							$t("AUTH.LOGIN")
						}}</span>
						<Loader2Icon v-else class="w-8 h-8 me-2 animate-spin" />
					</Button>
					<!-- <Button class="h-[var(--dashboard-input-height)] w-full" variant="outline"> Login with Google </Button> -->
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
