import { createRouter, createWebHistory } from 'vue-router'
import publicRoutes from './public.routes'
import rootRoutes from './root.routes'
import authRoutes from './auth.routes'
import dashboardRoutes from './dashboard.routes'

const routes = [
	...authRoutes,
	{
		path: '/dashboard',
		name: 'publicIndex',
		component: import('../views/dashboard/DashboardView.vue'),
		children: dashboardRoutes,
	}, {
		path: '/r00t',
		name: 'rootIndex',
		component: import('../views/root/RootView.vue'),
		children: rootRoutes,
	},
	{
		path: '/',
		name: 'publicIndex',
		component: import('../views/public/IndexView.vue'),
		children: publicRoutes
	},
	{
		path: '/:pathMatch(.*)*',
		redirect: '/'
	}
]

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes
})

export default router
