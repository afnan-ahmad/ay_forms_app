<script setup>
import { ref } from 'vue'
import { extractSchema } from '@/client'
import { useCommonStore } from '@/stores/common'
import router from '@/router'
import DynamicForm from '@/components/DynamicForm.vue'

const { addForm } = useCommonStore()

const formTitle = ref('Form Title')
const formDescription = ref('The description for the form')
const fields = ref(null)

const generateDisabled = ref(true)
const inputFile = ref(null)
const handleFileChange = (e) => {
  generateDisabled.value = e.target.files.length !== 1
  inputFile.value = e.target.files[0]
}
const generate = async () => {
  const data = new FormData()
  data.append('input', inputFile.value)
  fields.value = await extractSchema(data)
}
const save = async (e) => {
  e.preventDefault()
  const success = addForm({ title: formTitle.value, description: formDescription.value, fields: fields.value })
  if (success) {
    router.replace('/')
  }
}
</script>

<template>
  <div class="flex-fill d-flex flex-row overflow-hidden">
    <div class="col col-4 p-4 overflow-hidden border-end">
      <form>
        <div class="mb-3">
          <label for="title" class="form-label">Form Title *</label>
          <input type="text" class="form-control" id="title" v-model="formTitle" />
        </div>
        <div class="mb-3">
          <label for="description" class="form-label">Description (optional)</label>
          <input type="text" class="form-control" id="description" v-model="formDescription" />
        </div>
        <div class="mb-3">
          <label for="inputFile" class="form-label">Upload spreadsheet *</label>
          <div class="input-group mb-3">
            <input type="file" class="form-control" id="inputFile" name="inputFile" @change="handleFileChange" />
            <button @click="generate" class="btn btn-secondary" type="button" :disabled="generateDisabled">Generate Form</button>
          </div>
          <div class="form-text">
            <span>Supported file formats are XLSX and CSV.</span>
          </div>
        </div>
        <button type="submit" @click="save" class="btn btn-primary">Save</button>
      </form>
    </div>
    <div class="col col-8 overflow-auto bg-body p-4">
      <h2>{{ formTitle }}</h2>
      <p class="fs-5">{{ formDescription }}</p>
      <DynamicForm :fields="fields"></DynamicForm>
    </div>
  </div>
</template>
