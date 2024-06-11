import { createRouter, createWebHistory } from "vue-router"
import publicRoutes from "./public.routes"
import rootRoutes from "./root.routes"
import authRoutes from "./auth.routes"
import dashboardRoutes from "./dashboard.routes"

import type { IUsers } from "@/_interfaces/users.interface"

const routes = [
	{
		path: "/",
		name: "publicIndex",
		component: import("../views/public/IndexView.vue"),
		children: publicRoutes
	},
	{
		path: "/auth",
		name: "authIndex",
		component: import("../views/auth/AuthIndexView.vue"),
		children: authRoutes
	},
	{
		path: "/dashboard",
		name: "dashboardIndex",
		component: import("../views/dashboard/DashboardIndexView.vue"),
		children: dashboardRoutes,
		meta: {
			requiresAuth: true
		}
	},
	{
		path: "/r00t",
		name: "rootIndex",
		component: import("../views/root/RootView.vue"),
		children: rootRoutes,
		meta: {
			requiresAuth: true,
			isSuperUSer: true
		}
	},
	{
		path: "/:pathMatch(.*)*",
		redirect: "/"
	}
]

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes
})

router.beforeEach((to, from, next) => {
	console.log(to, from)
	if (!to.matched.find((record) => record.meta.requiresAuth)) return next()
	// ----------------------------------------------------------------
	const currentUser: IUsers = JSON.parse(localStorage.getItem("currentUser") || "{}")
	if (!currentUser?.access_token) return next({ name: "login" })
	if (to.matched.find((record) => record.meta.isSuperUSer) && !currentUser.is_root)
		return next({ name: "login" })
	next()
})

export default router
