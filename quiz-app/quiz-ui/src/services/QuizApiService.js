import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestion(position) {
    return this.call("get", "questions?position="+position)
  },
  rebuildDB() {
    return this.call("post", "rebuild-db");
  },
  login(password) {
    const data = { password: password };
    return this.call("post", "login", data);
  },
  postQuestion(question) {
    return this.call("post", "questions", question);
  },
  deleteQuestion(questionId) {
    return this.call("delete", "questions/" + questionId);
  },
  deleteAllQuestions() {
    return this.call("delete", "questions/all");
  },
  getQuestionById(questionId) {
    return this.call("get", "questions/" + questionId);
  },
  updateQuestion(questionId, question) {
    return this.call("put", "questions/" + questionId, question);
  },
  deleteAllParticipants() {
    return this.call("delete", "participations/all");
  },
  postParticipants(participants) {
    return this.call("post", "participations", participants);
  }
};