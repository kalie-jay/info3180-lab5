<template>
  <div class="container">
    <div v-if="successMsg" class="alert alert-success">{{ successMsg }}</div>
    <div v-if="errors.length" class="alert alert-danger" role="alert">
      <ul class="mb-0">
        <li v-for="error in errors" :key="error">{{ error }}</li>
      </ul>
    </div>

    <form id="movieForm" @submit.prevent="saveMovie">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" name="title" class="form-control" required />
      </div>

      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea name="description" class="form-control" required></textarea>
      </div>

      <div class="form-group mb-3">
        <label for="poster" class="form-label">Photo Upload</label>
        <input type="file" name="poster" class="form-control" accept="image/*" required />
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let csrf_token = ref("");
let successMsg = ref("");
let errors = ref([]);

function getCsrfToken() {
    fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log("CSRF Token received");
            csrf_token.value = data.csrf_token;
        });
}

onMounted(() => {
    getCsrfToken();
});

function saveMovie() {
    console.log("Submit button clicked!");
    
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);

    fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value
        }
    })
    .then(async response => {
        const data = await response.json();
        
        if (response.status === 201) {
            successMsg.value = data.message;
            errors.value = [];
            movieForm.reset();
        } else {
            errors.value = data.errors || [data.message || "An error occurred"];
            successMsg.value = "";
        }
    })
    .catch(error => {
        console.error("Fetch Error:", error);
        errors.value = ["Could not connect to the server."];
    });
}
</script>

<style scoped>
h1 {
  font-weight: bold;
  margin-bottom: 20px;
}
.alert ul {
  padding-left: 20px;
}
</style>