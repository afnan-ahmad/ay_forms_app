<script setup>
const props = defineProps(['form'])
</script>

<template>
  <div class="card border-0 shadow-sm">
    <div class="card-body">
      <div class="d-flex mb-2">
        <div class="d-flex flex-column flex-fill">
          <span class="card-title flex-grow-1 fw-bolder mb-0">{{ props.form.title }}</span>
          <span class="flex-grow-1">{{ props.form.description }} </span>
        </div>
        <span class="text-end text-muted">{{ props.form.submissions || 0 }} responses</span>
      </div>
    </div>
    <router-link :to="{ name: 'form', params: { id: props.form.id } }" class="stretched-link"></router-link>
  </div>
</template>
