<script setup>
import { ref } from 'vue'
import { storeToRefs } from 'pinia'
import { getSubmissions, createSubmission, getUsers } from '@/client'
import { useCommonStore } from '@/stores/common'
import { useAuthStore } from '@/stores/auth'
import { useRoute } from 'vue-router'
import router from '@/router'
import DynamicForm from '@/components/DynamicForm.vue'

const { user } = storeToRefs(useAuthStore())
const { getFormById } = useCommonStore()
const { params } = useRoute()

const form = ref(null)
const submissions = ref(null)
const availableUsers = ref(null)

const frm = getFormById(params.id)
if (!frm) {
  router.replace('/')
} else {
  form.value = frm
  getSubmissions(frm.id).then((data) => {
    submissions.value = data
  })
  getUsers().then((data) => {
    availableUsers.value = data
  })
}

const getUserEmailById = (id) => {
  return availableUsers.value.find((x) => x.id == id).email
}

const handleSubmit = async (data) => {
  const submission = await createSubmission({
    form_id: frm.id,
    data: data,
  })
  if (submission) {
    submissions.value.push(submission)
  }
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
          <button class="nav-link" id="submissions-tab" data-bs-toggle="tab" data-bs-target="#submissions-tab-pane" type="button" role="tab">
            Submissions
          </button>
        </li>
      </ul>
      <div class="tab-content bg-body border-start border-end h-100 overflow-auto" id="myTabContent">
        <div class="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0">
          <div class="col col-12 col-md-8 mx-auto p-4">
            <h2>{{ form.title }}</h2>
            <p class="fs-5">{{ form.description }}</p>
            <DynamicForm :fields="form.fields" :show-submit="true" v-on:submit="handleSubmit"></DynamicForm>
          </div>
        </div>
        <div class="tab-pane fade" id="submissions-tab-pane" role="tabpanel" aria-labelledby="submissions-tab" tabindex="0">
          <div class="col col-12 p-4">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col" v-if="user.is_admin">User</th>
                  <th scope="col">Created at</th>
                  <th scope="col" v-for="field in form.fields" :key="field">{{ field.label }}</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="submission in submissions" :key="submission">
                  <th scope="row" v-if="user.is_admin">{{ getUserEmailById(submission.user_id) }}</th>
                  <td>{{ submission.created_at }}</td>
                  <td v-for="field in submission.data" :key="field">{{ field }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
