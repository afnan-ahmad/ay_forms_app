<script setup>
import { useAuthStore } from '@/stores/auth';
import { storeToRefs } from 'pinia';

const { user } = storeToRefs(useAuthStore());

</script>

<template>
  <nav class="navbar navbar-expand bg-body shadow-sm p-2 position-relative z-3">
    <div class="container-fluid px-2">
      <router-link to="/" class="navbar-brand align-middle fw-bolder">AY Forms</router-link>
      <ul v-if="user" class="navbar-nav">
        <li class="nav-item dropdown align-middle">
          <button class="btn btn-link nav-link shadow-none dropdown-toggle p-0 me-2" data-bs-toggle="dropdown">
            <strong class="me-2">{{ user.email }}</strong>
          </button>
          <ul class="dropdown-menu dropdown-menu-end shadow">
            <li>
              <router-link to="/logout" class="dropdown-item">Logout</router-link>
            </li>
          </ul>
        </li>
      </ul>
    </div>
  </nav>
</template>
