import {} from "vue-router"
// import  from '../views/public/HomeView.vue'

const publicRoutes = [
	{
		path: "/",
		name: "home",
		component: () => import("../views/public/HomeView.vue")
	},
	{
		path: "/projects",
		name: "projects",
		component: () => import("../views/public/ProjectsView.vue")
	},
	{
		path: "/accelerator",
		name: "accelerator",
		component: () => import("../views/public/AcceleratorView.vue")
	},
	{
		path: "/projects/:itemId",
		name: "projectsView",
		component: () => import("../views/public/ProjectItemView.vue")
	},
	{
		path: "/about",
		name: "about",
		component: () => import("../views/public/AboutView.vue")
	},
	{
		path: "/404",
		name: "404",
		component: () => import("../views/public/404View.vue")
	}
]
export default publicRoutes
