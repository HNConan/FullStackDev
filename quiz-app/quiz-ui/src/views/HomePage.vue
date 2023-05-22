<template>

  <div class="title">
    <h1 class="titleBox">Langage de Programmation Quizz</h1>
  </div>

<div class = "ScoreArray" > 
      <table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Player</th>
      <th scope="col">Score</th>
    </tr>
  </thead>
  <tbody>
      <tr v-for="(scoreEntry, index) in registeredScores" v-bind:key="scoreEntry.date">
        <th scope="row">{{ index + 1 }}</th>
        <td>{{ scoreEntry.playerName }}</td>
        <td>{{ scoreEntry.score }}</td>
    </tr>
  </tbody>
</table>

</div>
                

  <div class = "BeginQuizz">
    <router-link class = "goToNewQuizz" to="/NewQuizPage"> Démarrer le quiz !</router-link>
  </div>
</template>

<style>
.title {
  justify-content: top;
  align-items: center;
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
  justify-content: center;
  align-items: center;
  height: 25; /* Ajustez cette valeur selon vos besoins */

}

.BeginQuizz
{
  display: flex;
  justify-content: center;
  align-items: flex-end;
  padding-bottom: 2rem; /* Ajustez selon vos besoins */
}
.goToNewQuizz
{
  text-align: center;

}
.dataTab
{
  display: flex;
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

  }
    
</script>
