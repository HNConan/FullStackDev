<template>
  <div class="m-5">
    <h1 class="titleBox m-5"><u class="bg-warning p-3 titleText"><b>Langage de Programmation Quizz</b></u></h1>
  </div>

  <div class="container-fluid bg-image"></div>

  <div class="container TopPlayers">
    <div class="ArrayTitle ">
      <h2 class="titleA">Top Players :</h2>
    </div>
    <div class="ScoreArray">
      <table class="table">
        <thead>
          <tr class="table-light">
            <th scope="col">#</th>
            <th scope="col">Player</th>
            <th scope="col">Score</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(scoreEntry, index) in registeredScores" :key="scoreEntry.date" v-show="index < 5"
            :class="getRowClass(index)">
            <th scope="row">{{ index + 1 }}</th>
            <td>{{ scoreEntry.playerName }}</td>
            <td>{{ scoreEntry.score }}</td>
          </tr>
        </tbody>
      </table>


    </div>
  </div>



  <div class="BeginQuizz">
    <router-link class="goToNewQuizz btn btn-lg btn-success mt-2" to="/NewQuizPage"><b>Démarrer le quiz
        !</b></router-link>
  </div>
</template>

<style>
.titleBox {
  text-align: center;
  white-space: nowrap;
  color: black;
}

th {
  font-weight: bold;
}

.TopPlayers {
  background-color: #a1a1a141;
  border-radius: 1rem;
  padding: 0.7rem;
}

.titleText {
  border-radius: 1rem;
}

.scoreEntry {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 25;
  /* Ajustez cette valeur selon vos besoins */

}

.BeginQuizz {
  display: flex;
  justify-content: center;
  align-items: flex-end;
}

.goToNewQuizz {
  border: 2px solid red;
  text-align: center;
  font-size: 30px;
  color: rgb(255, 255, 255);
}


.dataTab {
  display: flex;
}

.titleA {
  text-align: center;

}

.titleBox,
.dataTab,
.titleA,
.scoreEntry {
  color: black;
}

.row-color-0 {
  background-color: gold;
  /* Couleur de fond pour les autres lignes */
}

.row-color-1 {
  background-color: silver;
  /* Couleur de fond pour les 3 premières lignes */
}

.row-color-2 {
  background-color: rgb(205, 127, 50);
  /* Couleur de fond pour les autres lignes */
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
  methods: {
    getRowClass(index) {
      if (index < 3) {
        return 'row-color-' + index; // Classe CSS pour les 3 premières lignes
      } else {
        return 'table-light'; // Classe CSS par défaut pour les autres lignes
      }
    },
  },

}

</script>
