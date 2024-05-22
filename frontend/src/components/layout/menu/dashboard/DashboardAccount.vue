<script setup lang="ts">
import { Avatar, AvatarFallback, AvatarImage } from "@/shared/shadcn-ui/ui/avatar"
import { Button } from "@/shared/shadcn-ui/ui/button"
import {
	DropdownMenu,
	DropdownMenuContent,
	DropdownMenuGroup,
	DropdownMenuItem,
	DropdownMenuLabel,
	DropdownMenuSeparator,
	DropdownMenuShortcut,
	DropdownMenuTrigger
} from "@/shared/shadcn-ui/ui/dropdown-menu"
</script>

<template>
	<DropdownMenu>
		<DropdownMenuTrigger as-child>
			<Button variant="default" class="relative h-8 w-8 bg-accent rounded-full">
				<Avatar class="h-8 w-8 bg-accent">
					<AvatarImage src="../../../assets/logo.png" alt="@shadcn" />
					<AvatarFallback>TN</AvatarFallback>
				</Avatar>
			</Button>
		</DropdownMenuTrigger>
		<DropdownMenuContent class="w-56" align="end">
			<DropdownMenuLabel class="font-normal flex">
				<div class="flex flex-col space-y-1">
					<p class="text-sm font-medium leading-none">shadcn</p>
					<p class="text-xs leading-none text-muted-foreground">m@example.com</p>
				</div>
			</DropdownMenuLabel>
			<DropdownMenuSeparator />
			<DropdownMenuGroup>
				<DropdownMenuItem>
					Profile
					<DropdownMenuShortcut>⇧⌘P</DropdownMenuShortcut>
				</DropdownMenuItem>
				<DropdownMenuItem>
					Billing
					<DropdownMenuShortcut>⌘B</DropdownMenuShortcut>
				</DropdownMenuItem>
				<DropdownMenuItem>
					Settings
					<DropdownMenuShortcut>⌘S</DropdownMenuShortcut>
				</DropdownMenuItem>
				<DropdownMenuItem>New Team</DropdownMenuItem>
			</DropdownMenuGroup>
			<DropdownMenuSeparator />
			<DropdownMenuItem>
				Log out
				<DropdownMenuShortcut>⇧⌘Q</DropdownMenuShortcut>
			</DropdownMenuItem>
		</DropdownMenuContent>
	</DropdownMenu>
</template>
