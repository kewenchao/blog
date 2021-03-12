<template>
  <div class="header">
    <router-link to="/">首页</router-link>
    <router-link to="/category">分类</router-link>
    <router-link to="/about"> 关于</router-link>
  </div>
</template>


<script>
export default {
  name: "Header",
};
</script>

<style>
.header {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
}
</style>