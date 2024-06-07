import { createRouter, createWebHistory } from 'vue-router'
import publicRoutes from './public.routes'
import rootRoutes from './root.routes'
import authRoutes from './auth.routes'
import dashboardRoutes from './dashboard.routes'
import type { IUsers } from '@/interfaces/users.interface'

const routes = [
	{
		path: '/auth',
		name: 'authIndex',
		component: import('../views/auth/AuthIndexView.vue'),
		children: authRoutes,
	},
	{
		path: '/auth/:pathMatch(.*)*',
		redirect: '/auth/login'  // Redirect any unknown /auth routes to /auth/login
	},
	{
		path: '/dashboard',
		name: 'dashboardIndex',
		component: import('../views/dashboard/DashboardIndexView.vue'),
		children: dashboardRoutes,
		meta: {
			requiresAuth: true,
		}
	}, {
		path: '/r00t',
		name: 'rootIndex',
		component: import('../views/root/RootView.vue'),
		children: rootRoutes,
		meta: {
			requiresAuth: true,
			isSuperUSer: true,
		}
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

router.beforeEach((to, from, next) => {
	// console.log(to, from)
	if (!to.matched.some(record => record.meta.requiresAuth)) next();
	// ----------------------------------------------------------------
	const currentUser: IUsers = JSON.parse(localStorage.getItem('currentUser') || '{}')
	if (!currentUser?.access_token)
		return next({ name: 'login' });
	if (to.matched.some(record => record.meta.isSuperUSer) && !currentUser.is_root)
		return next({ name: 'login' });
	next();
});

export default router
