<script setup lang="ts">
import { defineEmits } from "vue"
import { cn } from "@/libs/utils"
import Icon from "@/shared/components/Icon.vue"
import { ScrollArea, Button } from "@/shared/shadcn-ui/ui"

export interface DashboardLinks {
	path: string
	icon: string
	label: string
}

export interface DashboardCategories {
	title: string
	links: DashboardLinks[]
}

export interface SidebarProps {
	posts: string[]
	categories: DashboardCategories[]
	isCollapsed: boolean
}

defineProps<SidebarProps>()
const emit = defineEmits<{
	(e: "ontoggle"): void
}>()
</script>

<template>
	<TooltipProvider :delay-duration="0.1" :class="cn(isCollapsed && 'hidden')">
		<div
			:class="
				cn(
					'pb-12 bg-accent text-accent-foreground min-h-dvh border-e-[2px] border-e-primary',
					$attrs.class ?? ''
				)
			"
		>
			<div class="space-y-4 py-4">
				<div class="px-3 py-2" v-for="(item, index) in categories" :key="index">
					<h2 class="mb-2 px-4 text-lg font-semibold tracking-tight">{{ item.title }}</h2>
					<div class="space-y-1">
						<Button
							variant="link"
							class="w-full justify-start"
							v-for="(link, linkIndex) in item.links"
							:key="linkIndex"
						>
							<router-link class="flex justify-center items-start" :to="link.path">
								<Icon class="me-3" :size="18" :name="link.icon" /> {{ link.label }}
							</router-link>
						</Button>
					</div>
				</div>
				<div class="py-2">
					<h2 class="relative px-7 text-lg font-semibold tracking-tight">Posts</h2>
					<ScrollArea class="h-[300px] px-1">
						<div class="space-y-1 p-2">
							<Button
								v-for="(post, i) in posts"
								:key="`${post}-${i}`"
								variant="ghost"
								class="w-full justify-start font-normal"
							>
								<Icon name="Plug2Icon"></Icon>
								{{ post }}
							</Button>
						</div>
					</ScrollArea>
				</div>
			</div>
		</div>
	</TooltipProvider>
</template>
