<template>
  <div class="input-group mb-3">
    <label class="input-group-text" for="questionTitle">Titre :</label>
    <input v-model="question.title" type="text" class="form-control" id="questionTitle" name="questionTitle">
  </div>
  <div class="input-group mb-3">
    <label class="input-group-text" for="questionPosition">Position :</label>
    <input v-model.number="question.position" type="number" min="1" :max="(this.totalNumberOfQuest + 1).toString()"
      class="form-control" id="questionPosition" name="questionPosition">
  </div>
  <div class="input-group mb-3">
    <label class="input-group-text" for="questionText">Texte :</label>
    <textarea v-model="question.text" class="form-control" id="questionText" name="questionText"></textarea>
  </div>
  <div class="input-group mb-3">
    <label class="input-group-text" for="questionImage">Image actuelle :</label>
    <img :src="question.image" alt="Question Image" class="img-fluid">
  </div>
  <div class="input-group mb-3">
    <label class="input-group-text" for="questionImage">Nouvelle Image :</label>
    <ImageUpload @file-change="imageFileChangedHandler" />
  </div>
  <div>
    <h3>Réponses :</h3>
    <ul class="list-group">
      <li v-for="(answer, index) in question.possibleAnswers" :key="index" class="list-group-item">
        <div class="form-check">
          <label :for="'answerText' + index" class="form-check-label">Réponse {{ index + 1 }} :</label>
          <input v-model="answer.text" :id="'answerText' + index" :name="'answerText' + index" type="text"
            class="form-control">
          <label :for="'answerCorrect' + index" class="form-check-label">Correcte :</label>
          <input v-model="answer.isCorrect" :id="'answerCorrect' + index" :name="'answerCorrect' + index" type="checkbox"
            class="form-check-input">
        </div>
      </li>
    </ul>
  </div>
  <button @click="$emit('inputsOfQuest')" class="btn btn-primary mt-3">Enregistrer</button>
</template>

<script>
import ImageUpload from "@/views/ImageUpload.vue";
import quizApiService from "@/services/QuizApiService";

export default {
  name: 'QuestionAdminDisplay',
  emits: ['inputsOfQuest'],
  props: {
    question: {
      type: Object,
      required: true,
    },
  },
  created() {
    this.getNumberOfQuest();
  },
  computed: {
    maxQuestionPosition() {
      return this.totalNumberOfQuest + 1;
    },
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
      this.$emit('file-change', b64String);
    },
  },
  components: {
    ImageUpload,
  },
};
</script>
