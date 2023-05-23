<template>

    <div class="title">
      <h1 class="titleBox">Leaderboard</h1>
    </div>
  
  <div class="container-fluid bg-image" ></div>
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
  
  
  .bg-image {
    
    background-image: url("../assets/backgroundImage.jpeg"); /* Chemin d'accès relatif à partir du dossier "public" */
    background-size: cover;
    background-position: center;
    width: 100%;
    height: 100vh;
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;
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
    
    import('@/assets/backgroundImage.jpeg')
        .then((image) => {
          this.backgroundImage = image.default;
        })
        .catch((error) => {
          console.error(error);
        });
      },
  
    }
      
  </script>
  