<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <RouterLink class="navbar-brand" to="/">MovieApp</RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>
      
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <RouterLink class="nav-link" to="/">Home</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/">About</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/movies/create">Add Movie</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/movies">Movies</RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <RouterView /> </template>

<style>
body {
  padding-top: 75px;
}
</style>