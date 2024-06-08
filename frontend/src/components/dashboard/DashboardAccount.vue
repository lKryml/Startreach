<script setup lang="ts">
import { useRouter } from "vue-router"
import { Avatar, AvatarFallback, AvatarImage } from "@/shared/shadcn-ui/ui/avatar"
import { Button } from "@/shared/shadcn-ui/ui/button"
import {
	DropdownMenu,
	DropdownMenuContent,
	DropdownMenuGroup,
	DropdownMenuItem,
	DropdownMenuLabel,
	DropdownMenuSeparator,
	// DropdownMenuShortcut,
	DropdownMenuTrigger
} from "@/shared/shadcn-ui/ui/dropdown-menu"
import { useI18n } from "vue-i18n"
import { useAuthStore } from "@/stores/auth.store"
import { PowerOffIcon, User2Icon } from "lucide-vue-next"

const router = useRouter()
const { t } = useI18n()
const { logout, currentUser } = useAuthStore()
const whenLogouClicked = () => {
	router.push({ name: "login" })
	logout()
}
</script>

<template>
	<DropdownMenu>
		<DropdownMenuTrigger as-child>
			<Button variant="default" class="relative h-8 w-8 bg-accent rounded-full">
				<Avatar class="h-8 w-8 bg-secondary text-secondary-foreground">
					<AvatarImage src="../../../assets/logo.png" alt="@shadcn" />
					<AvatarFallback>{{ currentUser.first_name[0] }}</AvatarFallback>
				</Avatar>
			</Button>
		</DropdownMenuTrigger>
		<DropdownMenuContent class="w-56" align="end">
			<DropdownMenuLabel class="font-normal flex">
				<div class="flex flex-col space-y-1">
					<p class="text-sm font-medium leading-none">{{ currentUser.first_name }}</p>
					<p class="text-xs leading-none text-muted-foreground">
						{{ currentUser.email }}
					</p>
				</div>
			</DropdownMenuLabel>
			<DropdownMenuSeparator />
			<DropdownMenuGroup>
				<DropdownMenuItem>
					<span class="w-full h-full" @click="(e) => console.log(e)"
						>{{ t("USERS.PROFILE") }} <User2Icon
					/></span>
				</DropdownMenuItem>
			</DropdownMenuGroup>
			<DropdownMenuSeparator />
			<DropdownMenuItem>
				<span class="w-full h-full" @click="whenLogouClicked()"
					>{{ t("USERS.LOGOUT") }} <PowerOffIcon
				/></span>
				<!-- <DropdownMenuShortcut>⇧⌘Q</DropdownMenuShortcut> -->
			</DropdownMenuItem>
		</DropdownMenuContent>
	</DropdownMenu>
</template>
