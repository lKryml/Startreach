// import { RouteRecordRaw } from 'vue-router'

const dashboardRoutes = [
    {
        path: '',
        name: 'dashboardMainIndex',
        component: () => import('../views/dashboard/index/DashboardView.vue')
    }, {
        path: 'projects',
        name: 'dashboardProjects',
        component: () => import('../views/dashboard/projects/ProjectsView.vue')
    }, {
        path: 'projects/details',
        name: 'dashboardProjectsDetails',
        component: () => import('../views/dashboard/projects/ProjectsDetailsView.vue')
    }, {
        path: 'projects/details/:itemId',
        name: 'dashboardProjectsDetailsEdit',
        // props: true,
        component: () => import('../views/dashboard/projects/ProjectsDetailsView.vue')
    }, {
        path: 'webinars',
        name: 'dashboardWebinars',
        component: () => import('../views/dashboard/webinars/WebinarsView.vue')
    }, {
        path: 'webinars/details',
        name: 'dashboardWebinarsDetails',
        component: () => import('../views/dashboard/webinars/WebinarsDetailsView.vue')
    }, {
        path: 'webinars/details/:itemId',
        name: 'dashboardWebinarsDetailsEdit',
        // props: true,
        component: () => import('../views/dashboard/webinars/WebinarsDetailsView.vue')
    }, {
        path: 'posts',
        name: 'dashboardPosts',
        component: () => import('../views/dashboard/posts/PostsView.vue')
    }, {
        path: 'posts/details',
        name: 'dashboardPostsDetails',
        component: () => import('../views/dashboard/posts/PostsDetailsView.vue')
    }, {
        path: 'posts/details/:itemId',
        name: 'dashboardPostsDetailsEdit',
        // props: true,
        component: () => import('../views/dashboard/posts/PostsDetailsView.vue')
    }
]
export default dashboardRoutes;
