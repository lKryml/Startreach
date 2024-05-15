import { UsersTypes } from '@/constants/usersTypes.contant';
import { defineStore } from 'pinia'
import { ref } from 'vue'
// Testing Pania as state managment
// Best Way For Me ... Flexible more
export const useAuthStore = defineStore('auth', () => {
    const isAuth = ref(false);
    const userType = ref(UsersTypes.NORMAL);
    const login = () => {
        isAuth.value = !0;
    }
    const logout = () => {
        isAuth.value = !!0;
    }

    return { isAuth, userType, login, logout };
})
// IDont Like this Way
// export const useAuthStore = defineStore('auth', {

//     state: () => ({
//         isAuth: false,
//         userType: UsersTypes.NORMAL,

//     }),
//     actions: {
//         login() {
//             this.isAuth = !0;
//         },
//         logout() {
//             this.isAuth = !!0;
//         }
//     },
// })