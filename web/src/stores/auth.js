import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useSessionStorage } from '@vueuse/core'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const token = useSessionStorage('token', null)
  const isLoggedIn = computed(() => !!token.value)

  async function login(email, password) {
    const response = await fetch('http://localhost:5000/login?include_auth_token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email: email, password: password }),
    })

    const data = await response.json()

    if (!response.ok) {
      return {
        success: false,
        errors: data.response.errors,
      }
    }

    token.value = data.response.user.authentication_token

    return {
      success: true,
    }
  }

  async function getProfile() {
    const response = await fetch('http://localhost:5000/api/user', {
      method: 'GET',
      headers: {
        'Authentication-Token': token.value,
      },
    })

    const data = await response.json()

    if (!response.ok) {
      return
    }

    user.value = data
  }

  function logout() {
    token.value = null
    user.value = null
  }

  return { user, token, isLoggedIn, getProfile, login, logout }
})
