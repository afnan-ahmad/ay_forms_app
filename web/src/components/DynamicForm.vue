<script setup>
const props = defineProps(['fields'])
</script>

<template>
  <form>
    <div class="mb-3" v-for="field of props.fields" :key="field">
      <label :for="field.label" class="form-label">{{ field.label }}</label>
      <input :type="field.type" class="form-control" :id="field.label" />
    </div>
  </form>
</template>
