import { createRouter, createWebHistory } from 'vue-router'
import publicRoutes from './public.routes'
import rootRoutes from './root.routes'
import authRoutes from './auth.routes'
import dashboardRoutes from './dashboard.routes'

const routes = [
	...publicRoutes,
	...rootRoutes,
	...authRoutes,
	...dashboardRoutes,
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
