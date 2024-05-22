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
    }
]
export default dashboardRoutes;
