<script setup lang="ts">
import * as yup from "yup"
import ButtonBoxComponent from "@/shared/components/ButtonBoxComponent.vue"
import StepperComponent from "@/shared/components/StepperComponent.vue"
import { Input, Label } from "@/shared/shadcn-ui/ui/"
import { useI18n } from "vue-i18n"
import { ref, onBeforeMount } from "vue"
import { useRouter } from "vue-router"
import { useAuthStore } from "@/stores/auth.store"
import { useForm } from "vee-validate"
import { UsersTypesArray } from "@/constants/usersTypes.contant"

onBeforeMount(() => {
	// if (!authStore.isAuth) router.push("/auth/login")
})
const { t } = useI18n()
const authStore = useAuthStore()
const router = useRouter()
const currentStep = ref(1)
const authValidatorSchema = yup.object({
	user_type: yup.number().min(1).max(7).default(1),
	address: yup.string().min(2).max(300),
	email: yup.string().email(),
	phone: yup.string().min(9).max(10)
})
const { errors, defineField, handleSubmit } = useForm({
	validationSchema: authValidatorSchema
})
const getError = (field: string) => errors.value?.[field] as string
const [userType, userTypeAttrs] = defineField("user_type")
const [phone, phoneAttrs] = defineField("phone")
const [address, addressAttrs] = defineField("address")
const [email, emailAttrs] = defineField("email")
const onSubmitForm = async (_values: any) => {}
const onSubmitFormErrors = () => {}
const onSubmit = handleSubmit(onSubmitForm, onSubmitFormErrors)
</script>
<template>
	<form @submit.prevent="onSubmit" class="w-full h-dvh grid lg:min-h-[600px] xl:min-h-[800px]">
		<StepperComponent
			:steps="['usertype', 'info', 'address']"
			:default-step="currentStep"
			@onnext="(step) => (currentStep = step)"
			@onpreviuos="(step) => (currentStep = step)"
		>
			<div
				class="flex flex-row gap-2 items-stretch justify-center flex-wrap w-full lg:w-[650px]"
			>
				<ButtonBoxComponent
					v-show="currentStep === 1"
					class="lg:min-w-[160px] xl:min-w-[200px]"
					v-for="(item, index) in UsersTypesArray"
					:key="index"
					:description="t(item.description)"
					:title="t(item.title)"
					:img="item.img"
					:isActive="item.id === userType"
					@change="userType = item.id"
				></ButtonBoxComponent>

				<div class="flex justify-center items-center" v-show="currentStep === 2">
					<div class="grid gap-4">
						<div class="grid gap-2">
							<Label for="phone">{{ $t("USERS.PHONE") }}</Label>
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
							<Label for="address">{{ $t("USERS.ADDRESS") }}</Label>
							<Input
								v-model="address"
								v-bind="addressAttrs"
								id="address"
								type="address"
								placeholder="0910000000"
								v-bind:class="{ 'border-destructive': getError('address') }"
							/>
						</div>
						<div class="grid gap-2">
							<Label for="email">{{ $t("USERS.EMAIL") }}</Label>
							<Input
								v-model="email"
								v-bind="emailAttrs"
								id="email"
								type="email"
								placeholder="0910000000"
								v-bind:class="{ 'border-destructive': getError('email') }"
							/>
						</div>
					</div>
				</div>
			</div>
		</StepperComponent>
	</form>
</template>
