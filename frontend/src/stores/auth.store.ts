import type { IUsers } from '@/interfaces/users.interface';
import { defineStore } from 'pinia'
import { ref } from 'vue'
// Testing Pania as state managment
// Best Way For Me ... Flexible more
export const useAuthStore = defineStore('auth', () => {
    const currentUser = ref<IUsers>(JSON.parse(localStorage.getItem('currentUser') || '{}'));
    const isAuth = ref<boolean>(!!currentUser.value?.access_token);
    const userType = ref<number>();
    const login = (user: IUsers) => {
        currentUser.value = user;
        if (user?.access_token) {
            isAuth.value = !!user.profile_id;
            localStorage.setItem('currentUser', JSON.stringify(user));
            localStorage.setItem('access_token', user.access_token);
        } else {
            logout();
        }
    }
    const logout = () => {
        isAuth.value = !!0;
        localStorage.removeItem('currentUser');
        localStorage.removeItem('access_token');
    }

    return { isAuth, userType, currentUser, login, logout };
})