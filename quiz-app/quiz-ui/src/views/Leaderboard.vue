<template>
  <div class="container bg-warning leaderBoard">
    <div class="title">
      <h1 class="titleBox"><u><b>Leaderboard :</b></u></h1>
      <h4 class="titleBox">Classement des participations</h4>
    </div>
    <div class="titleBox  m-4" v-if="this.playerScore != null">
      <h3>
        <span class="bg-success score text-white p-3"><b><u>Votre score :</u> {{ this.playerScore
        }}</b></span>
      </h3>
    </div>

    <div class="container-fluid bg-image"></div>
    <div class="ScoreArray">
      <table class="table table-success table-striped">
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
  </div>
</template>
  
<style>
.score {
  border-radius: 1rem;
}

.title {
  justify-content: top;
  align-items: center;
  height: 100px;
}

.leaderBoard {
  border-radius: 1rem !important;
  padding: 1rem !important;
}

.titleBox {
  text-align: center;
  white-space: nowrap;


}

.scoreEntry {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 25;
}




.dataTab {
  display: flex;
}

.titleBox,
.dataTab,
.titleA,
.scoreEntry {
  color: black;
}

.bg-image {

  background-image: url("../assets/backgroundImage.jpeg");
  /* Chemin d'accès relatif à partir du dossier "public" */
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
import participationApiService from "@/services/ParticipationStorageService";

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
    this.playerName = participationApiService.getPlayerName();
    this.playerScore = participationApiService.getParticipationScore();
    console.log(this.playerScore);
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
  