<template>
  <div>
    <h2>Question : {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h2>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
  </div>
</template>
  
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
          participationStorageService.clear();
          this.$router.push('./');
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>