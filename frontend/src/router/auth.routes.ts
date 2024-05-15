// import { RouteRecordRaw } from 'vue-router'

const authRoutes = [
    {
        path: '/auth',
        name: 'authroot',
        redirect: '/auth/login'
    },
    {
        path: '/auth/login',
        name: 'login',
        component: () => import('../views/auth/LoginView.vue')
    },
    {
        path: '/auth/register',
        name: 'register',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/auth/RegisterView.vue')
    }
]
export default authRoutes;
