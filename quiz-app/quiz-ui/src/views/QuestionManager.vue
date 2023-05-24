<template>
  <div class="container-fluid bg-image"></div>

  <div class="bg-success text-dark p-5 m-5 bigDiv border-warning ">
    <h2>
      <span class="bg-warning p-2 currQuest"><b><u>Question :</u> {{ currentQuestionPosition }} / {{ totalNumberOfQuestion
      }}</b></span>
    </h2>
    <h3 class="mt-3 ms-1">Sélectionner la bonne réponse :</h3>
    <div class="QuestionPart p-1 m-5">
      <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
    </div>
  </div>
</template>
<style>
.QuestionPart {
  background-color: rgba(0, 0, 0, 0.103);
  border-radius: 2rem;
}

.currQuest {
  border-radius: 1rem;
}

.bigDiv {
  border: 1rem solid white;
  border-radius: 3rem;
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
import QuestionDisplay from "@/views/QuestionDisplay.vue";
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: 'QuestionManager',
  components: {
    QuestionDisplay,
  },
  data() {
    return {
      currentQuestion: {},
      currentQuestionPosition: 1,
      totalNumberOfQuestion: 10,
    };
  },
  created() {
    this.loadQuestionByPosition();
    quizApiService.getQuizInfo()
      .then((response) => {
        this.totalNumberOfQuestion = response.data['size'];
      })
      .catch((error) => {
        console.error(error);
      });
  },
  methods: {
    async loadQuestionByPosition() {
      try {
        const position = this.currentQuestionPosition;
        const response = await quizApiService.getQuestion(position);
        this.currentQuestion = response.data;
        this.currentQuestionPosition = position;
      } catch (error) {
        console.error(error);
      }
    },
    answerClickedHandler(answerPosition) {
      // Gérer la réponse sélectionnée par l'utilisateur
      let answers = participationStorageService.getPlayerAnswers();
      answers.splice(this.currentQuestionPosition - 1, 1, answerPosition);
      participationStorageService.savePlayerAnswers(answers);
      if (this.currentQuestionPosition == this.totalNumberOfQuestion) {
        this.endQuiz();
      } else {
        this.goToNextQuestion()
      }
    },
    goToNextQuestion() {
      this.currentQuestionPosition = parseInt(this.currentQuestionPosition) + 1
      this.loadQuestionByPosition()
    },
    endQuiz() {
      const playerName = participationStorageService.getPlayerName();
      const answers = participationStorageService.getPlayerAnswers();
      // Créer un nouvel objet avec les propriétés playerName et answers
      const jsonData = {
        playerName: playerName,
        answers: answers
      };
      // Convertir l'objet en une chaîne de caractères JSON
      const jsonString = JSON.stringify(jsonData);
      // Gérer la fin du quiz
      quizApiService.postParticipants(jsonString)
        .then((response) => {
          participationStorageService.savePlayerName(response.data['playerName']);
          participationStorageService.saveParticipationScore(response.data['score']);
          this.$router.push('./Leaderboard');
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>