<template>
  <div class="container bg-white">
    <h1 style="color:black">Tableau des Questions</h1>
    <table class="table table-striped text-start">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Position</th>
          <th scope="col">Titre</th>
          <th scope="col">Texte</th>
          <th scope="col">Image</th>
          <th scope="col">Réponses</th>
          <th scope="col">Modifier</th>
          <th scope="col">Supprimer</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(question, index) in questions" :key="index">
          <td>{{ question.id }}</td>
          <td>{{ question.position }}</td>
          <td>{{ question.title }}</td>
          <td>{{ question.text }}</td>
          <td>
            <img :src="question.image" alt="Question Image" class="img-fluid">
          </td>
          <td>
            <ul class="list-unstyled">
              <li v-for="(answer, answerIndex) in question.possibleAnswers" :key="answerIndex">
                <u v-if="answer.isCorrect">
                  <p>{{ answer.position + 1 }} : {{ answer.text }}</p>
                </u>
                <p v-if="!answer.isCorrect">{{ answer.position + 1 }} : {{ answer.text }}</p>
              </li>
            </ul>
          </td>
          <td>
            <router-link :to="`/question/${question.id}/edit`" class="btn btn-primary">Modifier</router-link>
          </td>
          <td>
            <button @click="deleteQuestion(question.id)" class="btn btn-danger">Supprimer</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: 'QuestionTable',
  data() {
    return {
      questions: [],
    };
  },
  created() {
    this.getQuestions();
  },
  methods: {
    getQuestions() {
      quizApiService.getQuizInfo()
        .then((response) => {
          const numQuestion = response.data['size'];
          for (let i = 1; i <= numQuestion; i++) {
            this.fetchQuestion(i);
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    fetchQuestion(index) {
      quizApiService.getQuestion(index)
        .then((response) => {
          this.questions.push(response.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    deleteQuestion(questionId) {
      // Envoyer une requête API pour supprimer la question avec l'ID donné
      quizApiService.deleteQuestion(questionId)
        .then((response) => {
          // Supprimer la question de la liste
          this.questions = this.questions.filter(question => question.id !== questionId);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
