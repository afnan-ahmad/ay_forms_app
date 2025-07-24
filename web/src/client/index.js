import { storeToRefs } from 'pinia'
import { useAuthStore } from '@/stores/auth'

export async function extractSchema(formData) {
  const { token } = storeToRefs(useAuthStore())

  const response = await fetch('http://localhost:5000/api/extract', {
    method: 'POST',
    body: formData,
    headers: {
      'Authentication-Token': token.value,
    },
  })

  return await response.json()
}

export async function getForms() {
  const { token } = storeToRefs(useAuthStore())

  const response = await fetch('http://localhost:5000/api/forms', {
    method: 'GET',
    headers: {
      'Authentication-Token': token.value,
    },
  })

  return await response.json()
}

export async function createForm(form) {
  const { token } = storeToRefs(useAuthStore())

  const response = await fetch('http://localhost:5000/api/forms', {
    method: 'POST',
    body: JSON.stringify(form),
    headers: {
      'Authentication-Token': token.value,
      'Content-Type': 'application/json',
    },
  })

  return await response.json()
}
