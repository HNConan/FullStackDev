<template>
  <h1>Question Displayer</h1>
  
</template>



<img v-if="question.image" :src="question.image" />

props: {
  question: {
    type: Object
  }
}
emits: ["answer-selected"]
<a @click="$emit('answer-selected', 2)">La réponse D</a>