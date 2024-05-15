// import { RouteRecordRaw } from 'vue-router'

const rootRoutes = [
    {
        path: '/300t',
        name: 'rootIndex',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/root/RootView.vue')
    }
]
export default rootRoutes;
