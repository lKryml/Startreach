import { } from 'vue-router'
// import  from '../views/public/HomeView.vue'

const publicRoutes = [
    {
        path: '/',
        name: 'home',
        component: import('../views/public/HomeView.vue')
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/public/AboutView.vue')
    }
]
export default publicRoutes;
