
<template >
  <div> 
    <h1> QuestionDisplay</h1>
    <p>Question Title : {{ question.QuestionTitle }}</p>
    <currentQuestion /> 

  </div>

</template>

<script> 
export default
{
  name: 'QuestionDisplay',
    emits: ["answer-selected"],

    props: {
        question: {
            type: Object,
         
        }
    },
    methods: {
        selectAnswer(possibleAnswerIndex) {
            this.$emit('answer-selected', possibleAnswerIndex + 1);
        }
    },
}


</script>
