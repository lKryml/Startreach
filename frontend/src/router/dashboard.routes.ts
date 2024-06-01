// import { RouteRecordRaw } from 'vue-router'

const dashboardRoutes = [
    {
        path: '',
        name: 'dashboardMainIndex',
        component: () => import('../views/dashboard/DashboardView.vue')
    }, {
        path: 'projects',
        name: 'dashboardProjects',
        component: () => import('../views/dashboard/ProjectsView.vue')
    }, {
        path: 'projects/details',
        name: 'dashboardProjectsDetails',
        component: () => import('../views/dashboard/ProjectsDetailsView.vue')
    }, {
        path: 'projects/details/:itemId',
        name: 'dashboardProjectsDetailsEdit',
        // props: true,
        component: () => import('../views/dashboard/ProjectsDetailsView.vue')
    }, {
        path: 'webinars',
        name: 'dashboardWebinars',
        component: () => import('../views/dashboard/WebinarsView.vue')
    }, {
        path: 'webinars/details',
        name: 'dashboardWebinarsDetails',
        component: () => import('../views/dashboard/WebinarsDetailsView.vue')
    }, {
        path: 'webinars/details/:itemId',
        name: 'dashboardWebinarsDetailsEdit',
        // props: true,
        component: () => import('../views/dashboard/WebinarsDetailsView.vue')
    }
]
export default dashboardRoutes;
