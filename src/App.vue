<template>
  <div id="app">
    <Header/>
    <router-view></router-view>
    <Footer/>
  </div>
</template>

<script>
import Header from "../src/components/Header";
import Footer from "../src/components/Footer";
export default {
  components: {
    Header,
    Footer,
  },
};
</script>

<style>
</style>
