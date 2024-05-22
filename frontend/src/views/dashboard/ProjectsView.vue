<template>
	<PanelTitle v-bind:title="t('MENU.PROJECTS')"></PanelTitle>
	dsad asd sad sad
</template>
<script setup lang="ts">
import PanelTitle from "@/components/layout/menu/PanelTitle.vue"
import { useI18n } from "vue-i18n"

const { t } = useI18n()
export interface PanelTitleProps {
	title: string
	icon?: string
}
defineProps<PanelTitleProps>()
</script>
