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
    console.log("Test get all scores");
    quizApiService.getQuizInfo()
      .then((response) => {
        this.registeredScores = response.data;
        this.registeredScores = Object.values(this.registeredScores['scores'])
      })
      .catch((error) => {
        console.error(error);
      });
    console.log("Composant Home page 'created'");
  },

};
</script>
