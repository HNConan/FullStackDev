<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <div class="wrapper">
    <HelloWorld msg="You did it!" />

    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <RouterLink to="/admin">Administration</RouterLink>
      <RouterLink to="/Leaderboard">Leaderboard</RouterLink>
    </nav>
  </div>
  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}



nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
  display: bottom;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

.wrapper {
  place-items: bottom;
  white-space: nowrap;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }





  nav {
    text-align: bottom;
    margin-left: -1rem;
    font-size: 1rem;
    display: bottom;
    padding: 1rem 0;
    margin-top: 1rem;
  }
}</style>
