<script setup lang="ts">
import { type Ref, defineProps, defineEmits } from "vue"
import { Button } from "@/shared/shadcn-ui/ui/button"
import { Tabs, TabsList, TabsTrigger } from "@/shared/shadcn-ui/ui/tabs"
import {
	DropdownMenu,
	DropdownMenuContent,
	DropdownMenuItem,
	DropdownMenuLabel,
	DropdownMenuSeparator,
	DropdownMenuTrigger
} from "@/shared/shadcn-ui/ui/dropdown-menu"
import { EyeIcon, EyeOff, File, ListFilter, PlusCircle } from "lucide-vue-next"
import { type ItemsToShowProps } from "@/components/layout/ActionTable.Component.vue"
interface TabsLinks {
	name: string
	path?: string
	label: string
}
interface FilterProps {
	tabs?: TabsLinks[]
	tabDefaultValue?: string
	addTitle?: string
	exportTitle?: string
	filterTitle?: string
	filterByTitle?: string
	itemsToShow?: ItemsToShowProps[]
}

const props = defineProps<FilterProps>()
const emit = defineEmits<{
	(e: "ontabclicked", tab: TabsLinks): void
	(e: "onexport"): void
	(e: "onfilter", filter: any): void
	(e: "onaddnew"): void
	(e: "onVisibilityChanged", items: FilterProps["itemsToShow"]): void
}>()
const buttonsSizes = "h-10 gap-3"

const onVisibilityChanged = (item: ItemsToShowProps) => {
	item.isHidden = !item.isHidden
	emit("onVisibilityChanged", props.itemsToShow)
}
</script>

<template>
	<Tabs default-value="tabDefaultValue">
		<div class="flex items-center">
			<TabsList>
				<TabsTrigger
					:class="buttonsSizes"
					v-for="(tab, index) of props.tabs"
					:key="index"
					:value="tab.name"
				>
					<template v-if="tab.path">
						<router-link :to="tab.path">{{ tab.label }}</router-link>
					</template>
					<template v-else>
						<span class="w-full h-full" @click="emit('ontabclicked', tab)">{{
							tab.label
						}}</span>
					</template>
				</TabsTrigger>
			</TabsList>
			<div class="ml-auto flex items-center gap-2">
				<DropdownMenu v-if="props.filterTitle && props.itemsToShow?.length">
					<DropdownMenuTrigger as-child>
						<Button variant="outline" size="sm" v-bind:class="buttonsSizes">
							<ListFilter class="h-3.5 w-3.5" />
							<span class="sr-only sm:not-sr-only sm:whitespace-nowrap">
								{{ props.filterTitle }}
							</span>
						</Button>
					</DropdownMenuTrigger>
					<DropdownMenuContent align="end">
						<DropdownMenuLabel v-if="props.filterByTitle">{{
							props.filterByTitle
						}}</DropdownMenuLabel>
						<DropdownMenuSeparator v-if="props.filterByTitle" />
						<DropdownMenuItem v-for="(item, index) of props.itemsToShow" :key="index">
							<span
								class="w-full h-full flex justify-start items-start"
								@click="onVisibilityChanged(item)"
							>
								<EyeIcon v-if="!item.isHidden" class="me-2 w-[14px]"></EyeIcon>
								<EyeOff v-else class="me-2 w-[14px]"></EyeOff>
								{{ item.label }}
							</span>
						</DropdownMenuItem>
					</DropdownMenuContent>
				</DropdownMenu>
				<span
					@click="
						(e) => {
							console.log(e)
							emit('onexport')
						}
					"
				>
					<Button size="sm" variant="outline" v-bind:class="buttonsSizes">
						<File class="h-3.5 w-3.5" />
						<span class="sr-only sm:not-sr-only sm:whitespace-nowrap">
							{{ props.exportTitle }}
						</span>
					</Button>
				</span>
				<span
					@click="
						(e) => {
							console.log(e)
							emit('onaddnew')
						}
					"
				>
					<Button size="sm" v-bind:class="buttonsSizes">
						<PlusCircle class="h-3.5 w-3.5" />
						<span class="sr-only sm:not-sr-only sm:whitespace-nowrap">
							{{ addTitle }}
						</span>
					</Button>
				</span>
			</div>
		</div>
	</Tabs>
</template>
