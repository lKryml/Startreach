<template>
	<div class="w-full h-dvh lg:grid lg:min-h-[600px] xl:min-h-[800px] lg:grid-cols-[350px_1fr]">
		<div class="hidden bg-muted lg:block">
			<div
				class="h-dvh w-full bg-[url('https://cdn.dribbble.com/userupload/12700543/file/original-2f761db0abe85c110884800f36395c9e.png?resize=1600x1200')] bg-[center_-283px]"
			></div>
		</div>
		<div class="flex items-strt flex-col justify-center">
			<div
				class="border-b-[1px] h-[60px] bg-accent text-accent-foreground border-b-border flex justify-end items-center px-10"
			>
				<router-link
					to="/"
					class="cursor-pointer py-2 px-6 rounded-full bg-primary text-primary-foreground hover:bg-secondary hover:text-secondary-foreground justify-center items-center flex flex-row-reverse"
					><ArrowLeft />العودة للرئيسية</router-link
				>
			</div>
			<router-view />
		</div>
	</div>
</template>
<script setup lang="ts">
import { ArrowLeft } from "lucide-vue-next"
</script>
