// import { RouteRecordRaw } from 'vue-router'

const authRoutes = [
    {
        path: 'login',
        name: 'login',
        component: () => import('../views/auth/LoginView.vue')
    },
    {
        path: 'register-completion',
        name: 'registercompletetion',
        component: () => import('../views/auth/RegisterCompletionView.vue')
    },
    {
        path: 'register',
        name: 'register',
        component: () => import(/* webpackChunkName: "about" */ '../views/auth/RegisterView.vue')
    },
    // {
    //     path: ":pathMatch(.*)*",
    //     redirect: "/auth/login" // Redirect any unknown /auth routes to /auth/login
    // },
]
export default authRoutes;
