<template>
  <div class="title">
    <h1 class="titleBox">Langage de Programmation Quizz</h1>
  </div>
  
  <div class ="scoreEntry" v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    
      {{ scoreEntry.playerName }} - {{ scoreEntry.score }}

  </div>
  <router-link to="/NewQuizPage"> Démarrer le quiz !</router-link>
</template>

<style>
.title {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  height: 50vh; /* Ajustez cette valeur selon vos besoins */
}
.titleBox
{
  text-align: left;
  white-space: nowrap;

}
.scoreEntry
{
  display: flex;
  justify-content: left;
  align-items: center;
  height: 25; /* Ajustez cette valeur selon vos besoins */

}
</style>

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
