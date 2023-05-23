export default {
  clear() {
    window.localStorage.clear();
  },
  saveTokenAdmin(TokenAdmin) {
    window.localStorage.setItem("Authorization", TokenAdmin);
  },
  getTokenAdmin() {
    return window.localStorage.getItem("Authorization");
  }
};