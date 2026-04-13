<template>
    <div class="container py-5">
        <h1 class="mb-4">Movies</h1>
        <div class="row row-cols-1 row-cols-md-3 g-4"> <div v-for="movie in movies" :key="movie.id" class="col">
                <div class="card h-100 shadow-sm"> <div class="poster-container">
                        <img :src="movie.poster" class="card-img-top poster-img" :alt="movie.title">
                    </div>

                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title fw-bold">{{ movie.title }}</h5>
                        <p class="card-text text-muted flex-grow-1">
                            {{ movie.description }}
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

const fetchMovies = () => {
    fetch('/api/v1/movies')
        .then(response => response.json())
        .then(data => {
            movies.value = data.movies;
        })
        .catch(error => console.log(error));
};

onMounted(() => {
    fetchMovies();
});
</script>

<style scoped>
.poster-container {
    height: 400px; 
    overflow: hidden;
}

.poster-img {
    width: 100%;
    height: 100%;
    object-fit: cover; 
    object-position: top;
}

.card-text {
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>