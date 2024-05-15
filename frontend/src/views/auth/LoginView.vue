<script lang="ts">
import { defineComponent } from "vue"
import { Button, Input, Label } from "@/shared/shadcn-ui/ui"
import { useAuthStore } from "@/stores/auth.store"

const authStore = useAuthStore()

export default defineComponent({
	components: { Button, Input, Label },
	beforeCreate() {
		if (authStore.isAuth) {
			console.log("Authenticated")
			this.$router.push("/dashboard")
		}
	},
	methods: {
		onSubmit() {
			authStore.login()
			alert("testing useAuthStore...Redirecting to Dashboard")
			this.$router.push("/dashboard")
		}
	},
	setup() {
		const authStore = useAuthStore()
		return { authStore }
	}
})
</script>

<template>
	<form
		@submit="onSubmit()"
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
						<Input id="email" type="email" placeholder="m@example.com" required />
					</div>
					<div class="grid gap-2">
						<div class="flex items-center">
							<Label for="password">{{ $t("USER.PASSWORD") }}</Label>
							<a
								href="/forgot-password"
								class="ml-auto inline-block text-sm underline"
							>
								{{ $t("AUTH.FORGOT_PASSWORD") }}
							</a>
						</div>
						<Input id="password" type="password" required />
					</div>
					<Button type="submit" class="w-full"> {{ $t("AUTH.LOGIN") }} </Button>
					<Button variant="outline" class="w-full"> Login with Google </Button>
				</div>
				<div class="mt-4 text-center text-sm">
					{{ $t("AUTH.DONT_HAVE_ACCOUNT") }}
					<a href="#" class="underline"> {{ $t("AUTH.REGISTER") }} </a>
				</div>
			</div>
		</div>
		<div class="hidden bg-muted lg:block">
			<div class="h-dvh w-full bg-gradient-to-bl from-violet-500 to-blue-500"></div>
		</div>
	</form>
</template>
