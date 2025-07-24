<script setup>
import { storeToRefs } from 'pinia'
import { useAuthStore } from '@/stores/auth'
import { useCommonStore } from '@/stores/common'
import FormCard from '@/components/FormCard.vue'

const { user } = storeToRefs(useAuthStore())
const { forms } = storeToRefs(useCommonStore())
</script>

<template>
  <div class="flex-fill d-flex flex-row overflow-hidden">
    <div class="flex-fill overflow-auto bg-secondary-body">
      <div class="pt-4 px-4 pb-2" v-if="user.is_admin">
        <router-link to="/create" class="btn btn-primary fw-bolder">Create Form</router-link>
      </div>
      <div class="d-flex flex-row flex-wrap mt-3">
        <div v-for="form in forms" :key="form.id" class="col-12 col-md-3 px-4">
          <FormCard :form="form"></FormCard>
        </div>
      </div>
    </div>
  </div>
</template>
