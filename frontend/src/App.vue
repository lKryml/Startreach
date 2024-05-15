<template>
	<div>
		<nav>
			<router-link class="ms-3" to="/">Home</router-link> |
			<router-link class="ms-3" to="/about">About</router-link>
			<router-link class="ms-3" to="/300t">Root</router-link>
			<router-link class="ms-3" to="/auth">Login</router-link>
			<router-link class="ms-3" to="/auth/register">Register</router-link>
			<router-link class="ms-3" to="/dashboard">Dashboard</router-link>
		</nav>
	</div>
	<router-view />
</template>

<script setup lang="ts">
import { defineComponent } from "vue"

defineComponent({
	setup() {
		return {
			msg: "/0x3oot"
		}
	}
})
</script>

<style>
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
