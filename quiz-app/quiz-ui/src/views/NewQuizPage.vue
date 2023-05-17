
<template>
  <h1>NewQuizz page</h1>
  <p class="text-start">Saisissez votre nom</p>
  <button type="button" class="btn btn-primary" @click="launchNewQuiz">Go</button>
  
  <div class="input-group mb-3">
    <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1"
      v-model="username">

  </div>
</template>
<script>
import participationStorageService from "../services/ParticipationStorageService";

let username = '';

export default {

  name: "NewQuizPage",

  methods: {
    launchNewQuiz() {

      console.log("Launch new quiz with", this.username);
      participationStorageService.savePlayerName(this.username);
      const playerName = participationStorageService.getPlayerName();
      this.$router.push('/QuestionDisplay');

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
