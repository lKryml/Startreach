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
        path: '/auth/register-completion',
        name: 'registercompletetion',
        component: () => import('../views/auth/RegisterCompletionView.vue')
    },
    {
        path: '/auth/register',
        name: 'register',
        component: () => import(/* webpackChunkName: "about" */ '../views/auth/RegisterView.vue')
    }
]
export default authRoutes;
