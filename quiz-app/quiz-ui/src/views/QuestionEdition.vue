<template>
  <div class="container" v-if="admin">
    <h2>Question : {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h2>
    <QuestionAdminDisplay :question="currentQuestion" @inputsOfQuest="saveQuestion"
      @file-change="imageFileChangedHandler" />
  </div>
</template>

<script>
import adminStorageService from "@/services/AdminStorageService";
import quizApiService from "@/services/QuizApiService";
import QuestionAdminDisplay from "@/views/QuestionAdminDisplay.vue";

export default {
  name: 'QuestionEdition',
  components: {
    QuestionAdminDisplay,
  },
  data() {
    return {
      currentQuestion: {
        title: '',
        position: '',
        text: '',
        image: '',
        possibleAnswers: [
          { text: '', isCorrect: false },
          { text: '', isCorrect: false },
          { text: '', isCorrect: false },
          { text: '', isCorrect: false },
        ],
      },
      currentQuestionPosition: 1,
      totalNumberOfQuestion: 10,
      currentQuestionID: 0,
    };
  },
  created() {
    if (adminStorageService.getTokenAdmin() != null) {
      this.admin = true;
    } else {
      this.admin = false;
    }
    const questionID = this.$route.params.id;
    this.loadQuestionByPosition(questionID);
    quizApiService.getQuizInfo()
      .then((response) => {
        this.totalNumberOfQuestion = response.data['size'];
      })
      .catch((error) => {
        console.error(error);
      });
  },
  methods: {
    async loadQuestionByPosition(questionID) {
      try {
        const response = await quizApiService.getQuestionById(questionID);
        this.currentQuestion = response.data;
        this.currentQuestionPosition = response.data['position'];
        this.currentQuestionID = response.data['id'];
      } catch (error) {
        console.error(error);
      }
    },
    async saveQuestion() {
      try {
        await quizApiService.updateQuestion(this.currentQuestionID, this.currentQuestion);
      } catch (error) {
        console.error(error);
      }
    },
    async imageFileChangedHandler(b64String) {
      this.currentQuestion.image = b64String;
    },
  },
}
</script>
