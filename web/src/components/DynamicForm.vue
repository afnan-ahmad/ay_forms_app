<script setup>
import { ref } from 'vue'

const props = defineProps(['fields', 'showSubmit'])
const emit = defineEmits(['submit'])

const data = ref({})

const handleCheckboxChange = (e) => {
  data.value[e.target.id] = e.target.checked
}

const handleSubmit = (e) => {
  e.preventDefault()

  if (!e.target.checkValidity()) {
    e.target.reportValidity()
  } else {
    emit('submit', data.value)
    e.target.reset()
  }
}
</script>

<template>
  <form @submit="handleSubmit">
    <div class="mb-3" v-for="field of props.fields" :key="field">
      <div class="form-check" v-if="field.type === 'checkbox'">
        <input class="form-check-input" type="checkbox" @change="handleCheckboxChange" :id="field.id" />
        <label class="form-check-label" :for="field.label"> {{ field.label }} </label>
      </div>
      <div v-else>
        <label :for="field.label" class="form-label">{{ field.label }}</label>
        <input :type="field.type" v-model="data[field.id]" class="form-control" :id="field.id" required />
      </div>
    </div>
    <button v-if="showSubmit" class="btn btn-primary" type="submit">Submit</button>
  </form>
</template>
