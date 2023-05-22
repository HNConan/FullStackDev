<template>
  <h1 class="header">Nouveau Quizz</h1>
  <h3 class="text-center">Saisissez votre nom</h3>
  <div class="d-flex flex-column align-items-center">
    <div class="mb-3">
      <button type="button" class="btn btn-primary" @click="launchNewQuiz">Go</button>
    </div>
    <div class="input-group">
      <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1"
        v-model="username">
    </div>
  </div>
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
  }

};
</script>
<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
