
<template>
    <h2>Question : {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h2>
    <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
</template>

<script>
import QuestionDisplay from "./QuestionDisplay.vue";
export default {
    name : 'QuestionManager',
    components:
    {
       currentQuestion:
        {
            QuestionTitle : "fdfdfd"
        }
    },

    data() {

        currentQuestion
        {
            QuestionTitle 
        }
        
        return {
            QuestionTitle,
            currentQuestion : {},
            playerAnswers : [],
            currentQuestionPosition : 1,
            totalNumberOfQuestion : 10
        };

    },
  
   async created() {

        this.property = 'Example property update.'

        console.log('propertyComputed will update, as this.property is now reactive.')

    },
    methods:
    {

        loadQuestionByPosition() {

        },
        answerClickedHandler() {

        },
        endQuiz() {

        }
    }
}
</script>
  