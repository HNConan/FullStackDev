<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header>
    <nav class="navbar navbar-dark sticky-top bg-success">
      <div class="container-fluid">
        <RouterLink class="nav-link links-menu" to="/">Accueil</RouterLink>
        <RouterLink class="nav-link links-menu" to="/Leaderboard">Leaderboard</RouterLink>
        <RouterLink class="nav-link links-menu" to="/about">About</RouterLink>
        <RouterLink class="nav-link links-menu" to="/admin">Administration</RouterLink>
      </div>
    </nav>
  </header>
  <main class="h-100">
    <div class="container mt-3 justify-content-center">
      <RouterView />
    </div>
  </main>
</template>

<style scoped>
nav {
  font-size: 1.2rem;
  padding: 1.5rem;
}

.links-menu {
  color: white;
}

nav a.router-link-exact-active {
  color: rgb(0, 0, 0);
  background-color: white;
}

a:hover {
  background-color: white !important;
  color: black;

}

nav a.router-link-exact-active:hover {
  background-color: white !important;
}

nav a {
  display: inline-block;
  padding: 0.1 2rem;
  border-radius: 1rem;
  text-decoration: none;
}

nav a:first-of-type {
  border: 0;
}
</style>
