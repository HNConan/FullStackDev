export default {
  clear() {
    window.localStorage.clear();
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    return window.localStorage.getItem("playerName");
  },
  savePlayerAnswers(playerAnswers) {
    window.localStorage.setItem("playerAnswers", JSON.stringify(playerAnswers));
  },
  getPlayerAnswers() {
    return JSON.parse(window.localStorage.getItem("playerAnswers")) || [];
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem("playerName", participationScore);
  },
  getParticipationScore() {
    return window.localStorage.getItem("participationScore");
  }
};