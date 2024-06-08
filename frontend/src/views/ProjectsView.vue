<template>
<div class="container-lg">
	<div class="flex w-full justify-center items-center align-self-end">
		<MenuComponent :items="menu" />
        <ProjectsComponent />
	</div>
	<router-view />
	</div>
</template>

<script setup lang="ts">

import MenuComponent from '@/components/menu/Menu.Component.vue';
import ProjectsComponent from '@/components/Projects.Component.vue';
import { menu } from "@/constants/menu/public.menu"
</script>