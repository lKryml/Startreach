<script setup lang="ts">
import { type Ref, defineEmits, defineProps } from "vue"
import Icon from "@/shared/components/Icon.vue"
import { datePickerFormat } from "@/_libs/date.utils"
import { MoreHorizontal } from "lucide-vue-next"
import { Button, Badge } from "@/shared/shadcn-ui/ui"
import {
	DropdownMenu,
	DropdownMenuContent,
	DropdownMenuItem,
	DropdownMenuSeparator,
	DropdownMenuLabel,
	DropdownMenuTrigger
} from "@/shared/shadcn-ui/ui/dropdown-menu"
import {
	Table,
	TableBody,
	TableCell,
	TableHead,
	TableHeader,
	TableRow
} from "@/shared/shadcn-ui/ui/table"
import { watch } from "vue"

export interface ItemsToShowProps {
	label?: string
	icon?: string
	value?: string
	isHidden?: boolean
	type: "text" | "img" | "badge" | "icon" | "date"
	isHideSm?: boolean
}
interface RowActionsProps {
	label?: string
	icon?: string
	action: string
	isHideLabel?: boolean
}
interface AnyMapsProps {
	[key: string]: {
		[key: string]: string
	}
}
interface ActionTableProps<T> {
	items: Array<T>
	itemsToShow: ItemsToShowProps[]
	actions?: Array<RowActionsProps>
	actionsTitle?: string
	imagesSize?: number
	iconsSize?: number
	iconsMaps?: AnyMapsProps
	badgesMaps?: AnyMapsProps
	dateFormat?: string
}
const props = defineProps<ActionTableProps<any>>()
const emit = defineEmits<{ (e: "onTableRowAction", action: string, payload: any): void }>()

watch(props.itemsToShow, (items) => console.log(items))

for (let i = 0; i < props.itemsToShow.length; i++) {
	if (props.itemsToShow[i].type === "date" && props.itemsToShow[i].value) {
		const key = props.itemsToShow[i].value as string
		props.items?.forEach((item: any) => {
			!(item[key] instanceof Date) ? (item[key] = new Date(item[key])) : undefined
		})
	}
}
</script>

<template>
	<Table>
		<TableHeader>
			<TableRow>
				<template v-for="(row, index) of props.itemsToShow" :key="index">
					<TableHead
						v-if="!row.isHidden && ['img', 'icon'].includes(row.type)"
						:class="row.isHideSm ? 'hidden  sm:table-cell' : ''"
					>
						<span class="sr-only">{{ row.type }}</span>
					</TableHead>
					<TableHead v-else-if="!row.isHidden">{{ row.label }}</TableHead>
				</template>
				<TableHead v-if="props.actions?.length">
					<span class="sr-only">{{ props.actionsTitle }}</span>
				</TableHead>
			</TableRow>
		</TableHeader>
		<TableBody>
			<TableRow v-for="item of props.items" :key="item.id">
				<template v-for="(row, index) of props.itemsToShow" :key="index">
					<TableCell
						v-if="!row.isHidden && row.type === 'img'"
						:class="row.isHideSm ? 'hidden  sm:table-cell' : ''"
					>
						<img
							class="aspect-square rounded-md object-cover"
							:alt="item.img"
							:height="props.imagesSize || 24"
							:width="props.imagesSize || 24"
							:src="item.img ? item.img : '../../assets/logo.png'"
						/>
					</TableCell>
					<template v-if="!row.isHidden && row?.value">
						<TableCell v-if="row.type === 'text'"
							><span class="w-full h-full">{{
								item[row?.value || ""]
							}}</span></TableCell
						>
						<TableCell v-else-if="row.type === 'badge'"
							><Badge variant="outline">{{
								props?.badgesMaps?.[row.value as any][item[row.value || ""]]
							}}</Badge></TableCell
						>
						<TableCell v-else-if="row.type === 'date'"
							><span class="w-full h-full">{{
								datePickerFormat(item[row?.value || ""])
							}}</span>
						</TableCell>
						<TableCell v-else
							><span class="w-full h-full"
								><Icon
									v-bind:name="
										props?.iconsMaps?.[row.value?.toString() as any][
											item[row.value?.toString() || '']
										] as any
									"
								></Icon></span
						></TableCell>
					</template>
					<template v-else-if="!row.isHidden">
						<TableCell></TableCell>
					</template>
				</template>
				<TableCell v-if="props.actions?.length">
					<DropdownMenu>
						<DropdownMenuTrigger as-child>
							<Button aria-haspopup="true" size="icon" variant="ghost">
								<MoreHorizontal class="h-4 w-4" />
								<span class="sr-only">Toggle menu</span>
							</Button>
						</DropdownMenuTrigger>
						<DropdownMenuContent align="end">
							<DropdownMenuLabel v-if="props.actionsTitle">{{
								props.actionsTitle
							}}</DropdownMenuLabel>
							<DropdownMenuSeparator
								v-if="props.actionsTitle"
							></DropdownMenuSeparator>
							<template v-for="(action, index) of props.actions" :key="index">
								<DropdownMenuItem
									><span
										class="w-full h-full"
										@click="emit('onTableRowAction', action.action, item)"
									>
										{{ action.label }}</span
									></DropdownMenuItem
								>
							</template>
						</DropdownMenuContent>
					</DropdownMenu>
				</TableCell>
			</TableRow>
		</TableBody>
	</Table>
</template>
