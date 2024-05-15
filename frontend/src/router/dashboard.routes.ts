// import { RouteRecordRaw } from 'vue-router'

const dashboardRoutes = [
    {
        path: '/dashboard',
        name: 'dashboardIndex',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/dashboard/DashboardView.vue')
    }
]
export default dashboardRoutes;
