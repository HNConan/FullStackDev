<template>
  <div class="about">
    <h1>Projet FullStack ESIEE 2023</h1>
    <h4> Réalisé par COMPAGNON Paul, CONAN Hadrien,BERTHELIN Joe  </h4>

  </div>
  <div class="container-fluid bg-image" ></div>

</template>

<style>
@media (min-width: 1024px) {
  .about {
    justify-content: top;
    align-items: center; 
     display: center;
     height: 100px;
     text-align: center;
     color: black; 

  }
  
.bg-image {
  
  background-image: url("../assets/backgroundImage.jpeg"); /* Chemin d'accès relatif à partir du dossier "public" */
  background-size: cover;
  background-position: center;
  width: 100%;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  z-index: -1;
}
  
}
</style>
<script>
export default {

 async created() {
  
  import('@/assets/backgroundImage.jpeg')
      .then((image) => {
        this.backgroundImage = image.default;
      })
      .catch((error) => {
        console.error(error);
      });
    }
  }
</script>
