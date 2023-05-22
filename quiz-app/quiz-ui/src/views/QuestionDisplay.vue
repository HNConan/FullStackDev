<template>
  <div>
    <h1><u>{{ question.title }}</u></h1>
    <h3>{{ question.text }}</h3>
    <div class="btn-group-vertical w-100 " role="group">
      <button @click="$emit('answer-selected', answer['position']+1)" v-for="(answer, index) in question.possibleAnswers" :key="index" class="btn btn-primary btn-group" type="button">{{answer['text']}}</button>
    </div>
   
    <currentQuestion />
  </div>
</template>

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
};
</script>