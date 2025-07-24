import { defineStore } from 'pinia'
import { ref } from 'vue'
import { getForms, createForm } from '@/client'

export const useCommonStore = defineStore('common', () => {
  const forms = ref(null)

  async function loadForms() {
    forms.value = await getForms()
  }

  async function addForm(form) {
    const newForm = await createForm(form)

    if (newForm) {
      forms.value.push(form)
      return true
    }

    return false
  }

  function getFormById(id) {
    return forms.value.find((x) => x.id == id)
  }

  return { forms, loadForms, addForm, getFormById }
})
