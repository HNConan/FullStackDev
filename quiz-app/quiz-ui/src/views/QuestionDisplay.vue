<template>
  <div class="m-2 p-3">
    <h1 class="text-center p-2">
      <span class="bg-success p-2 currQuest border border-2 border-warning"><b>{{ question.title }}</b></span>
    </h1>

    <h3 class="textQuest m-3 p-2">
      <span>{{ question.text }}</span>
    </h3>
    <div class="text-center"> <!-- Ajout de la classe text-center pour centrer l'image horizontalement -->
      <img :src="question.image" alt="Question Image" class="bg-warning p-1 m-2 rounded-5 img-fluid">
    </div>
    <div class="btn-group-vertical w-100" role="group">
      <button @click="$emit('answer-selected', answer['position'] + 1)"
        v-for="(answer, index) in question.possibleAnswers" :key="index"
        class="btn mb-2 mb-md-0 btn-answer btn-warning btn-block" type="button">{{ answer['text'] }}</button>
    </div>
    <currentQuestion />
  </div>
</template>

<style>
.currQuest {
  border-radius: 1rem;
}

.btn-answer:hover {
  background-color: rgba(10, 161, 10, 0.521);
  border-color: rgba(10, 161, 10, 0.521);
  transition: ease-out 0.5s;
}

.textQuest {
  font-weight: bold;
  color: white;
  background-color: rgba(0, 0, 0, 0.555);
  border-radius: 0.5rem;
}
</style>
<script>
export default {
  name: 'QuestionDisplay',
  emits: ['answer-selected'],
  props: {
    question: {
      type: Object,
      required: true,
    },
  },
  methods: {
    selectAnswer(possibleAnswerIndex) {
      this.$emit('answer-selected', possibleAnswerIndex + 1);
    },
  },
  async created() {

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