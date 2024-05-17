<template>
	<div
		path="{{ item.path }}"
		class="flex flex-row justify-center items-center"
		v-bind:class="{ 'text-muted-foreground': item.isDisabled, 'bg-muted': item.isDisabled }"
		v-show="item.label"
	>
		<router-link
			v-if="item.path"
			class="flex flex-row justify-center items-center w-auto mx-2"
			:to="item.path"
		>
			{{ t(item?.label || "") }}
			<span class="ms-1" v-show="item.icon"><item.icon :size="16"></item.icon></span>
		</router-link>
		<a
			v-else-if="item.url"
			class="flex flex-row justify-center items-center w-auto mx-2"
			:href="item.url"
		>
			{{ t(item?.label || "") }}
			<span class="ms-1" v-show="item.icon"><item.icon :size="16"></item.icon></span>
		</a>
		<Separator
			v-else-if="item.isSeparator"
			class="flex flex-row justify-center items-center w-auto"
		/>
	</div>
</template>
<script setup lang="ts">
import { type IMenuItem } from "@/interfaces/menu.interface"
import { Separator } from "@/shared/shadcn-ui/ui/separator"
import { defineProps } from "vue"
import { useI18n } from "vue-i18n"
const { t } = useI18n()
const { item } = defineProps<{ item: IMenuItem }>()
</script>
