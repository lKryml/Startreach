<template>
	<div class="w-full h-dvh lg:grid lg:min-h-[600px] xl:min-h-[800px] lg:grid-cols-[350px_1fr]">
		<div class="hidden bg-muted lg:block">
			<video
				src="https://cdn.dribbble.com/uploads/48226/original/b8bd4e4273cceae2889d9d259b04f732.mp4?1689028949"
				class="h-full object-cover w-full bg-[url('https://cdn.dribbble.com/uploads/48226/original/b8bd4e4273cceae2889d9d259b04f732.mp4?1689028949')] bg-[center_-283px]" autoplay loop="true" muted="true"
			></video>
		</div>
		
		<div class="flex items-center flex-col justify-start">
			
				
			
			<router-view class="relative"/>
			<router-link
					to="/"
					class="cursor-pointer  hover:text-secondary-foreground justify-center items-center flex flex-row-reverse self-start absolute left-1/4 top-52"
					><PanelRightOpenIcon class="w-[24px] me-2 text-secondary hover:text-primary "></PanelRightOpenIcon></router-link
				>
		</div>
	</div>
</template>
<script setup lang="ts">
import { ArrowLeft } from "lucide-vue-next"
import { PanelRightOpenIcon, SendIcon } from "lucide-vue-next"
</script>
