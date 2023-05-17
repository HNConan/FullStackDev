
<template>
    <h1>Question Manager</h1>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
</template>

<script>
export default {

    data() {

        currentQuestion:
        {
            QuestionTitle = "";
            QuestionText = "";
            QuestionText = "";
            possibleAnswers = [];
        }
        currentQuestionPosition: 1
        return {


        }

    },
    components: {
        QuestionDisplay
    },
    created() {

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
  