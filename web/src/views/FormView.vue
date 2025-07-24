<script setup>
import { ref } from 'vue'
import { useCommonStore } from '@/stores/common'
import { useRoute } from 'vue-router'
import router from '@/router'
import DynamicForm from '@/components/DynamicForm.vue'

const { getFormById } = useCommonStore()
const { params } = useRoute()

const form = ref(null)

const frm = getFormById(params.id)
if (frm) {
  form.value = frm
} else {
  router.replace('/')
}
</script>

<template>
  <div class="flex-fill d-flex flex-row overflow-hidden">
    <div class="col col-12 p-4 overflow-hidden">
      <ul class="nav nav-tabs" id="myTab" role="tablist">
        <li class="nav-item" role="presentation">
          <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab">{{ form.title }}</button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab">Submissions</button>
        </li>
      </ul>
      <div class="tab-content bg-body border-start border-end h-100 overflow-auto" id="myTabContent">
        <div class="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0">
          <div class="col col-12 col-md-8 mx-auto p-4">
            <h2>{{ form.title }}</h2>
            <p class="fs-5">{{ form.description }}</p>
            <DynamicForm :fields="form.fields"></DynamicForm>
          </div>
        </div>
        <div class="tab-pane fade" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabindex="0">...</div>
      </div>
    </div>
  </div>
</template>
