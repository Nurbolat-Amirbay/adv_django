import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/LoginPanel.vue';
import Admin from '../views/AdminPanel.vue';
import Register from '../views/RegisterPanel.vue';
import { useStore } from 'vuex';
import { computed } from 'vue';

const store = useStore();

const routes = [
    { path: '/', component: Login },
    { path: '/register', component: Register },
    {
        path: '/admin',
        component: Admin,
        meta: { requiresAdmin: true },
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach(async (to, from, next) => {
    if (to.meta.requiresAdmin) {
        if (!store.state.user) {
            await store.dispatch('fetchUser');
        }

        const userRole = computed(() => store.state.user?.role);

        if (userRole.value === 'admin') {
            next();
        } else {
            next('/');
        }
    } else {
        next();
    }
});

export default router;
