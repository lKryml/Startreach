<script setup lang="ts">
import { ref } from "vue"
import {
	Breadcrumb,
	BreadcrumbItem,
	BreadcrumbLink,
	BreadcrumbList,
	BreadcrumbPage,
	BreadcrumbSeparator
} from "@/shared/shadcn-ui/ui/breadcrumb"
import { onBeforeMount } from "vue"
import { useI18n } from "vue-i18n"
export interface BreadCrumbLinks {
	path: string
	label: string
}
export interface PanelTitleProps {
	title: string
	icon?: string
	isBreadcrumb?: boolean
	breadcrumbLinks?: BreadCrumbLinks[]
}

const { t } = useI18n()
const { isBreadcrumb, breadcrumbLinks } = defineProps<PanelTitleProps>()
const tempBreadcrumbLinks = ref(breadcrumbLinks || [])

onBeforeMount(() => {
	if (isBreadcrumb) {
		if (
			tempBreadcrumbLinks.value.length &&
			!tempBreadcrumbLinks.value[0].path.startsWith("dashboard")
		) {
			tempBreadcrumbLinks.value.unshift({
				path: "",
				label: t("MENU.DASHBOARD")
			})
		}
	}
})
</script>
<template>
	<header
		class="sticky top-0 z-30 flex h-14 items-start gap-4 border-b px-4 sm:static sm:h-auto sm:border-0 sm:px-6"
	>
		<Breadcrumb class="hidden md:flex">
			<BreadcrumbList>
				<template v-for="(link, index) in tempBreadcrumbLinks" :key="index">
					<BreadcrumbItem>
						<BreadcrumbLink as-child>
							<router-link :to="link.path">{{ link.label }}</router-link>
						</BreadcrumbLink>
					</BreadcrumbItem>
					<template v-if="index < tempBreadcrumbLinks.length - 1">
						<BreadcrumbSeparator />
					</template>
				</template>
			</BreadcrumbList>
		</Breadcrumb>
	</header>
</template>
