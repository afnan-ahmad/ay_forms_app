import { createRouter, createWebHashHistory } from 'vue-router'

import LoginView from '@/views/LoginView.vue'
import HomeView from '@/views/HomeView.vue'
import CreateView from '@/views/CreateView.vue'
import FormView from '@/views/FormView.vue'

import { useAuthStore } from '@/stores/auth'
import { useCommonStore } from '@/stores/common'

const routes = [
  {
    path: '/login',
    name: 'login',
    meta: {
      title: 'Login',
    },
    component: LoginView,
  },
  {
    path: '/',
    name: 'home',
    meta: {
      title: 'Home',
    },
    component: HomeView,
  },
  {
    path: '/create',
    name: 'create',
    meta: {
      title: 'Create',
    },
    component: CreateView,
  },
  {
    path: '/form/:id',
    name: 'form',
    meta: {
      title: 'Form',
    },
    component: FormView,
  },
]

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  linkActiveClass: 'active',
  routes,
})

router.beforeEach(async (to, from, next) => {
  const goingToAuthenticatedRoute = to.name !== 'login' && to.name !== 'register'
  const goingToLoginOrRegister = to.name === 'login' || to.name === 'register'

  const { isLoggedIn, user, getProfile, logout } = useAuthStore()
  const { forms, loadForms, clearForms } = useCommonStore()

  if (isLoggedIn && !user) {
    await getProfile()
  }

  if (isLoggedIn && !forms) {
    await loadForms()
  }

  if (goingToAuthenticatedRoute && !isLoggedIn) {
    return next({ name: 'login' })
  }

  if (goingToLoginOrRegister && isLoggedIn) {
    return next({ name: 'home' })
  }

  if (to.path === '/logout' && isLoggedIn) {
    clearForms()
    logout()
    return next({ name: 'login' })
  }

  if (to.name === 'create' && !user.is_admin) {
    return next({ name: 'home' })
  }

  return next()
})

router.afterEach((to) => {
  document.title = to.meta.title + ' | AY Forms'
})

export default router
