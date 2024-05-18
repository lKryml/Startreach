import { UsersTypes } from '@/constants/usersTypes.contant';
import type { IUsers } from '@/interfaces/users.interface';
import { defineStore } from 'pinia'
import { ref } from 'vue'
// Testing Pania as state managment
// Best Way For Me ... Flexible more
export const useAuthStore = defineStore('auth', () => {
    const isAuth = ref(false);
    const currentUser = ref<IUsers>();
    const userType = ref(UsersTypes.NORMAL);
    const login = (user: IUsers) => {
        currentUser.value = user;
        isAuth.value = !!user?.access_token;
        if (isAuth.value) {
            localStorage.setItem('currentUser', JSON.stringify(user));
        } else {
            logout();
        }
    }
    const logout = () => {
        isAuth.value = !!0;
        localStorage.removeItem('currentUser');
    }

    return { isAuth, userType, login, logout, currentUser };
})