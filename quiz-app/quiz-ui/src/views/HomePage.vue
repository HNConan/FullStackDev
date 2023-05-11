<template>
  <h1>Home page</h1>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  <router-link to="/NewQuizPage"> Démarrer le quiz !</router-link>
</template>


<script>
import quizApiService from "@/services/QuizApiService";
import { registerRuntimeCompiler } from "vue";
let registeredScores = [];
export default {
  name: "HomePage",
  data() {
    return {
      registeredScores,
    };
  },
  async created() {
    registeredScores = QuizApiService.getQuestion(),
      console.log("Composant Home page 'created'");
  }

};
</script>
