<script setup lang="ts">
import { defineEmits, defineProps } from "vue"
import {
	AlertDialog,
	AlertDialogAction,
	AlertDialogCancel,
	AlertDialogContent,
	AlertDialogDescription,
	AlertDialogFooter,
	AlertDialogHeader,
	AlertDialogTitle
	// AlertDialogTrigger
} from "@/shared/shadcn-ui/ui/alert-dialog"
const props = defineProps<{
	isOpen: boolean
	title: string
	description: string
	cancelText: string
	actionText: string
	actionVariant: "destructive" | "default" | "secondary"
}>()
const emit = defineEmits<{
	(e: "oncancel"): void
	(e: "onaction"): void
}>()
</script>

<template>
	<AlertDialog :open="props.isOpen" :default-open="false">
		<!-- <AlertDialogTrigger>{{ triggerText }}</AlertDialogTrigger> -->
		<AlertDialogContent>
			<AlertDialogHeader>
				<AlertDialogTitle>{{ props.title || "Are you absolutely sure?" }}</AlertDialogTitle>
				<AlertDialogDescription>
					{{
						props.description ||
						"This action cannot be undone. This will permanently delete your account and remove your data from our servers."
					}}
				</AlertDialogDescription>
			</AlertDialogHeader>
			<AlertDialogFooter>
				<AlertDialogCancel
					><span class="w-full h-full m-0 p-0" @click="emit('oncancel')">{{
						props.cancelText
					}}</span></AlertDialogCancel
				>
				<AlertDialogAction
					:class="
						actionVariant === 'destructive'
							? 'bg-destructive text-destructive-foreground'
							: actionVariant === 'secondary'
								? 'bg-secondary text-secondary-foreground'
								: ''
					"
					><span class="w-full h-full m-0 p-0" @click="emit('onaction')">{{
						props.actionText
					}}</span></AlertDialogAction
				>
			</AlertDialogFooter>
		</AlertDialogContent>
	</AlertDialog>
</template>
