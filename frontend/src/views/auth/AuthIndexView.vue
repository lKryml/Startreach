<template>
	<div class="w-full h-dvh lg:grid lg:min-h-[600px] xl:min-h-[800px] lg:grid-cols-[350px_1fr]">
		<div class="hidden bg-muted lg:block">
			<video
				src="https://cdn.dribbble.com/uploads/48226/original/b8bd4e4273cceae2889d9d259b04f732.mp4?1689028949"
				class="h-full object-cover w-full bg-[url('https://cdn.dribbble.com/uploads/48226/original/b8bd4e4273cceae2889d9d259b04f732.mp4?1689028949')] bg-[center_-283px]"
				autoplay
				loop="true"
				muted="true"
			></video>
		</div>

		<div class="flex items-center flex-col justify-start w-full">
			<div class="flex items-center flex-col justify-start w-full">
				<div
					class="w-full border-b-[1px] h-[60px] text-accent-foreground border-b-border flex justify-end items-center px-10"
				>
					<router-link
						to="/"
						class="cursor-pointer py-2 px-6 rounded-full bg-primary text-primary-foreground hover:bg-secondary hover:text-secondary-foreground justify-center items-center flex flex-row-reverse"
						><ArrowRight />Homepage</router-link
					>
				</div>
				<router-view />
			</div>
		</div>
	</div>
</template>
<script setup lang="ts">
import { ArrowRight } from "lucide-vue-next"
import { PanelRightOpenIcon, SendIcon } from "lucide-vue-next"
</script>
