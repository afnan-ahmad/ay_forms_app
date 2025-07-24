<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import router from '@/router'

const { login } = useAuthStore()

const loggingIn = ref(false)
const errors = ref(null)

const email = ref('admin@test.com')
const password = ref('Test@123')

const handleLogin = async (e) => {
  e.preventDefault()

  loggingIn.value = true

  const result = await login(email.value, password.value)

  if (result.success) {
    router.replace('/')
  } else {
    errors.value = result.errors
    loggingIn.value = false
  }
}
</script>

<template>
  <div class="d-flex align-items-center justify-content-center h-100">
    <div class="col-11 col-md-3 bg-body rounded shadow-sm p-4 mb-5">
      <h3 class="fw-bold mb-3">Login</h3>
      <ul v-if="errors">
        <li v-for="error in errors" :key="error">{{ error }}</li>
      </ul>
      <form class="mt-3" id="login_user_form" action="#">
        <div class="mb-3">
          <label class="form-label" for="email">Email</label>
          <input v-model="email" class="form-control" type="email" id="email" name="email" :disabled="loggingIn" required />
        </div>
        <div class="mb-3">
          <label class="form-label" for="password">Password</label>
          <input v-model="password" class="form-control" type="password" id="password" name="password" :disabled="loggingIn" required />
        </div>
        <div class="text-end">
          <button type="submit" @click="handleLogin" class="btn btn-primary" :disabled="loggingIn">
            <span v-if="loggingIn" class="spinner-border spinner-border-sm"></span>
            Login
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
