<script setup lang="ts">
import { defineProps, defineEmits } from "vue"
import {
	Pagination,
	PaginationEllipsis,
	PaginationFirst,
	PaginationLast,
	PaginationList,
	PaginationListItem,
	PaginationNext,
	PaginationPrev
} from "@/shared/shadcn-ui/ui/pagination"

import { Button } from "@/shared/shadcn-ui/ui/button"

interface PaginationProps {
	total?: number
	currentPage?: number
	itemsPerpage?: number
	disabled?: boolean
}
const props = defineProps<PaginationProps>()
const emit = defineEmits<{ (e: "onpagechanged", _page: number): void }>()
const totalPages = Math.ceil((props.total || 0) / (props.itemsPerpage || 1))
</script>

<template>
	<Pagination
		v-slot="{ page }"
		:total="props.total"
		:sibling-count="1"
		show-edges
		:default-page="1"
		:items-per-page="props.itemsPerpage"
		@update:page="(_page: number) => emit('onpagechanged', _page)"
	>
		<PaginationList v-slot="{ items }" class="flex items-center gap-1" v-if="totalPages > 1">
			<PaginationFirst />
			<PaginationPrev />

			<template v-for="(item, index) in items">
				<PaginationListItem
					v-if="item.type === 'page'"
					:key="index"
					:value="item.value"
					as-child
				>
					<Button
						class="w-10 h-10 p-0"
						:variant="item.value === page ? 'default' : 'outline'"
					>
						{{ item.value }}
					</Button>
				</PaginationListItem>
				<PaginationEllipsis v-else :key="item.type" :index="index" />
			</template>

			<PaginationNext />
			<PaginationLast />
		</PaginationList>
	</Pagination>
</template>
