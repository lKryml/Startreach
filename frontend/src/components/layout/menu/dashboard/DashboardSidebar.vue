<script setup lang="ts">
import { defineEmits } from "vue"
import { cn } from "@/_libs/utils"
import Icon from "@/shared/components/Icon.vue"
import { ScrollArea, Button } from "@/shared/shadcn-ui/ui"
import { PanelRightOpenIcon, SendIcon } from "lucide-vue-next"
import { Sheet, SheetContent, SheetTrigger } from "@/shared/shadcn-ui/ui/sheet"

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
	addPostsTitle: string
	appName: string
}

defineProps<SidebarProps>()
const emit = defineEmits<{
	(e: "ontoggle"): void
}>()
</script>

<template>
	<TooltipProvider :delay-duration="0.1" :class="cn(isCollapsed && 'hidden')">
		<Sheet>
			<SheetTrigger as-child>
				<Button size="icon" variant="outline" class="lg:hidden absolute top-[10px] start-3">
					<PanelRightOpenIcon class="h-5 w-5" />
					<span class="sr-only">Toggle Menu</span>
				</Button>
			</SheetTrigger>
			<SheetContent side="right" class="sm:max-w-xs">
				<nav class="grid gap-6 text-lg font-medium">
					<a
						href="#"
						class="group flex h-10 w-10 shrink-0 items-center justify-center gap-2 rounded-full bg-primary text-lg font-semibold text-primary-foreground md:text-base"
					>
						<SendIcon class="h-5 w-5 transition-all group-hover:scale-110" />
						<span class="sr-only">Team</span>
					</a>
					<template v-for="(_item, index) in categories" :key="index">
						<router-link
							v-for="(link, _index) of _item.links"
							:key="_index"
							:to="link.path"
							class="flex items-center gap-4 px-2.5 text-muted-foreground hover:text-foreground"
						>
							<Icon :name="link.icon" class="h-5 w-5" />
							{{ link.label }}
						</router-link>
					</template>
				</nav>
			</SheetContent>
		</Sheet>
		<div
			:class="
				cn(
					'fixed inset-y-0 left-0 z-10 hidden w-[var(--sidebar-width)] start-0 top-0 flex-col border-e-[1px] border-sidebar-border bg-sidebar text-sidebar-foreground lg:flex',
					$attrs.class ?? ''
				)
			"
		>
			<ScrollArea class="w-full space-y-4 pb-4">
				<div
					class="h-[var(--dashboard-navbar-height)] flex justify-center items-center font-extrabold text-xl border-b-[1px] border-border mb-8"
				>
					<PanelRightOpenIcon class="w-[24px] me-2"></PanelRightOpenIcon>
					{{ appName }}
				</div>
				<div
					class="px-3 py-2 border-b-[1px] border-border"
					v-for="(item, index) in categories"
					:key="index"
				>
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
					<div class="px-1" v-if="posts?.length">
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
					</div>
					<div v-else class="flex justify-start items-center m-5">
						<router-link to="/dashboard/posts/details">
							<Button class="text-sm">
								<Icon name="PlusCircleIcon" class="me-1"></Icon>
								{{ addPostsTitle }}
							</Button>
						</router-link>
					</div>
				</div>
			</ScrollArea>
		</div>
	</TooltipProvider>
</template>
