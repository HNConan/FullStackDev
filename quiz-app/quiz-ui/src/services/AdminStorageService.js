export default {
  clear() {
    window.localStorage.clear();
  },
  saveTokenAdmin(TokenAdmin) {
    window.localStorage.setItem("Authorization", TokenAdmin);

    // Planifie la suppression du token après 3600 secondes
    setTimeout(() => {
      window.localStorage.removeItem('Authorization');
    }, 3600 * 1000);
  },
  getTokenAdmin() {
    return window.localStorage.getItem("Authorization");
  }
};