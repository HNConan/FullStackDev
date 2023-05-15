
<template>
  <h1>Question Displayer</h1>
  <img v-if="question.image" :src="question.image" />
  <a @click="$emit('answer-selected', 2)">La réponse D</a>

</template>
<script> 
export default
{
  props: {
  question: {
    type: Object,
  }
},
emits: {
    // No validation
    click: null,

    // Validate submit event
    submit: ({ email, password }) => {
      if (email && password) {
        return true
      } else {
        return false
      }
    }
  },
  methods: {
    emitFucntion()
    {
      this.$emit('answer-selected', 2);    
      
  }
}
}
</script>
