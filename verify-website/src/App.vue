<template>
  <div id="app">
    <!-- This is where the three cards are placed, each is a component -->
    <!-- Put up a loading screen first -->
    <!-- check if verified -->
    <!-- show the verified card with animation if verified-->
    <!-- show the doll card with loaded image and description -->
    <!-- show the footer card with links and logo and details -->
    <!-- if not verified dont show doll card -->
    <div @click="fetchData()">
      <head-card :verified="verified"></head-card>
    </div>
    <div v-if="verified">
      <doll-card :name="name" :description="description" :scannedDate="scannedDate"></doll-card>
    </div>
    <footer-card></footer-card>
  </div>
</template>

<script>
import DollCard from './components/DollCard.vue'
import HeadCard from './components/HeadCard.vue'
import FooterCard from './components/FooterCard.vue'
// Import axios here
// Once the app loads we want to fetch the data for the doll component
// Data will be shared with all components via this component
export default {
  name: 'App',
  data () {
    return {
      name: '',
      verified: false,
      description: '',
      scannedDate: ''
    }
  },
  components: {
    DollCard,
    HeadCard,
    FooterCard
  },
  methods: {
    fetchData () {
      this.verified = true
      this.name = 'Daniel'
      this.description = 'This is a description'
      this.scannedDate = '4/20/20'
    }
  }
}
</script>

<style>

/* We need a custom font that will be filled out here */
@import url('https://fonts.googleapis.com/css?family=Nunito&display=swap');
#app {
  font-family: 'Nunito', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
