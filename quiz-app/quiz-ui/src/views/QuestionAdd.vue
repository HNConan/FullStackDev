<template>
  <div class="container" v-if="admin">
    <h2 style="color: white;"><u>Ajouter une nouvelle question</u></h2>
    <div class="input-group mb-3">
      <label class="input-group-text" for="newQuestionTitle">Titre :</label>
      <input v-model="newQuestion.title" type="text" class="form-control" id="newQuestionTitle" name="newQuestionTitle">
    </div>
    <div class="input-group mb-3">
      <label class="input-group-text" for="newQuestionPosition">Position :</label>
      <input v-model.number="newQuestion.position" min="1" :max="(this.totalNumberOfQuest + 1).toString()" type="number"
        class="form-control" id="newQuestionPosition" name="newQuestionPosition">
    </div>
    <div class="input-group mb-3">
      <label class="input-group-text" for="newQuestionText">Texte :</label>
      <textarea v-model="newQuestion.text" class="form-control" id="newQuestionText" name="newQuestionText"></textarea>
    </div>
    <div class="input-group mb-3">
      <label class="input-group-text" for="newQuestionImage">Image :</label>
      <ImageUpload @file-change="imageFileChangedHandler" />
    </div>
    <div>
      <h3>Réponses :</h3>
      <ul class="list-group">
        <li v-for="(answer, index) in newQuestion.possibleAnswers" :key="index" class="list-group-item">
          <div class="form-check">
            <label :for="'answerText' + index" class="form-check-label">Réponse {{ index + 1 }} :</label>
            <input v-model="answer.text" :id="'answerText' + index" :name="'answerText' + index" type="text"
              class="form-control">
            <label :for="'answerCorrect' + index" class="form-check-label">Correcte :</label>
            <input v-model="answer.isCorrect" :id="'answerCorrect' + index" :name="'answerCorrect' + index"
              type="checkbox" class="form-check-input">
          </div>
        </li>
      </ul>
    </div>
    <div>
      <button @click="addQuestion" class="btn btn-primary">Ajouter</button>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import ImageUpload from "@/views/ImageUpload.vue";

export default {
  name: 'NewQuestion',
  components: {
    ImageUpload,
  },
  created() {
    this.getNumberOfQuest();
  },
  data() {

    return {
      newQuestion: {
        title: '',
        position: null,
        text: '',
        image: null,
        possibleAnswers: [
          { text: '', isCorrect: false },
          { text: '', isCorrect: false },
          { text: '', isCorrect: false },
          { text: '', isCorrect: false },
        ],
      },
    };
  },
  methods: {
    async getNumberOfQuest() {
      quizApiService.getQuizInfo()
        .then((response) => {
          this.totalNumberOfQuest = response.data['size'];
        })
        .catch((error) => {
          console.error(error);
        });
    },
    imageFileChangedHandler(b64String) {
      this.newQuestion.image = b64String;
    },
    addQuestion() {
      quizApiService.postQuestion(this.newQuestion)
        .then((response) => {
          console.log('Question added successfully');
          // Réinitialiser les valeurs
          this.newQuestion.title = '';
          this.newQuestion.position = null;
          this.newQuestion.text = '';
          this.newQuestion.image = null;
          this.newQuestion.possibleAnswers = [
            { text: '', isCorrect: false },
            { text: '', isCorrect: false },
            { text: '', isCorrect: false },
            { text: '', isCorrect: false },
          ];
          this.$router.push("/admin");
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
