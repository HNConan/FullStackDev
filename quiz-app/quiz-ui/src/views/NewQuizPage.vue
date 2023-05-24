<template>
  <div class="mainPage mt-3 text-success">
    <h1 class="text-center"><u><b>Saisissez votre nom</b></u></h1>
    <div class="d-flex flex-column align-items-center p-3">
      <div class="input-group">
        <label class="input-group-text bg-success text-light border-warning border-3" style=" font-size: 1.7rem;"
          for="questionImage">Pseudo :</label>
        <input type="text" class="form-control p-3 bg-secondary text-white" style="font-weight: bold; font-size: 2rem;"
          placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" v-model="username">
      </div>
      <div class="m-3">
        <button type="button" class="btn btn-lg btn-primary" @click="launchNewQuiz">Commencer le <b>Quizz</b></button>
      </div>
    </div>
  </div>
  <div class="container-fluid bg-image"></div>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

let username = '';

export default {

  name: "NewQuizPage",

  methods: {
    launchNewQuiz() {

      console.log("Launch new quiz with", this.username);
      participationStorageService.savePlayerName(this.username);
      const playerName = participationStorageService.getPlayerName();
      this.$router.push('./QuestionManager');

    }
  },
  async created() {
    participationApiService.clear();

    import('@/assets/backgroundImage.jpeg')
      .then((image) => {
        this.backgroundImage = image.default;
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
</script>
<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }

  .mainPage {
    text-align: center;
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
}
</style>
