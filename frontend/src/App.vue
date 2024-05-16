<template>
	<div>
		<nav>
			<Logo />
			<router-link class="ms-3" to="/">Home</router-link> |
			<router-link class="ms-3" to="/about">About</router-link>
			<router-link class="ms-3" to="/300t">Root</router-link>
			<router-link class="ms-3" to="/auth">Login</router-link>
			<router-link class="ms-3" to="/auth/register">Register</router-link>
			<router-link class="ms-3" to="/dashboard">Dashboard</router-link>
		</nav>
		<Separator />
	</div>
	<router-view />
</template>

<script setup lang="ts">
import { defineComponent } from "vue"
import { Separator } from "./shared/shadcn-ui/ui"
import Logo from "./components/svg/Logo.vue"

defineComponent({
	setup() {
		return {
			msg: "/0x3oot"
		}
	}
})
</script>

<style>
@font-face {
	font-family: "Aileron", sans-serif !important;
	src: url("/assets/fonts/Aileron-Black.otf") format("opentype");
	src: url("/assets/fonts/Aileron-Bold.otf") format("opentype");
	src: url("/assets/fonts/Aileron-Heavy.otf") format("opentype");
	src: url("/assets/fonts/Aileron-Light.otf") format("opentype");
	src: url("/assets/fonts/Aileron-Regular.otf") format("opentype");
	src: url("/assets/fonts/Aileron-Thin.otf") format("opentype");
	src: url("/assets/fonts/Aileron-UltraLight.otf") format("opentype");
}
html,
body {
	font-family: "Aileron", sans-serif !important;
	font-weight: 600;
}

nav {
	position: absolute;
	top: 0px;
	left: 0px;
	width: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	background: #fff;
	border-bottom: 1px solid #f1f1f1;
	height: 50px;
}
</style>
