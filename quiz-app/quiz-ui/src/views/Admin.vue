<template>
  <div>
    <h1>Partie Administration</h1>
    <div class="input-group mb-3 mt-3" v-if="!admin">
      <span class="input-group-text" id="basic-addon3">Mot de passe :</span>
      <input v-model="password" type="password" class="form-control" id="mdp-admin" name="mdp-admin"
        aria-describedby="mdp-admin">
      <button type="button" id="check" class="btn btn-primary" @click="passwordCheck">Connexion</button>
    </div>
    <div class="alert alert-danger" role="alert" v-if="errorMessage">{{ errorMessage }}</div>
    <div class="alert alert-info" role="alert" v-if="alreadyLoggedMessage">{{ alreadyLoggedMessage }}</div>
    <div class="alert alert-success" role="alert" v-if="successMessage">{{ successMessage }}</div>

    <div v-if="admin" class="text-center">
      <router-link class="btn m-3 btn-primary" to="/?">Ajouter une question</router-link>
      <QuestionList />

    </div>
  </div>
</template>

<script>
import adminStorageService from "@/services/AdminStorageService";
import quizApiService from "@/services/QuizApiService";
import QuestionList from "@/views/QuestionsList.vue";

export default {
  name: 'AdminVue',
  components: {
    QuestionList,
  },
  data() {
    return {
      password: '',
      errorMessage: '',
      alreadyLogged: '',
      successMessage: '',
      admin: false
    };
  },
  created() {
    if (adminStorageService.getTokenAdmin() != null) {
      this.admin = true;
    } else {
      this.admin = false;
    }

  },
  methods: {
    async passwordCheck() {
      const inputPassword = this.password; // Récupérer la valeur de l'input
      // Utiliser la valeur de l'input dans votre fonction passwordCheck()
      if (adminStorageService.getTokenAdmin() != null) {
        this.alreadyLogged = "Vous êtes déjà connecté !"
        return
      }
      quizApiService.login(inputPassword)
        .then((response) => {
          this.storeTokenAdmin(response.data['token']);
          this.errorMessage = '';
          this.alreadyLoggedMessage = '';
          this.password = '';
          this.admin = true;
        })
        .catch((error) => {
          this.alreadyLogged = '';
          this.password = '';
          this.errorMessage = "Mot de passe incorrect";
          console.error(error);
        });
      // ...
    },
    async storeTokenAdmin(token) {
      adminStorageService.saveTokenAdmin(token)
    },
  },
};
</script>
