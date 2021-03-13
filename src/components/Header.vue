<template>
  <div class="header">
    <img src="../assets/logo.png"> 
    <span>个人博客</span>
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
img{
  margin-top: 18px;
  height: 30px;
  margin-right: 5px;
}

.header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
  font-size: 20px;
  display: flex;
}
a{
  display: block;
  /* 距离20px */
  margin-left:20px;
  /* 去掉下划线 */
  text-decoration:none;
  color: black;
}
/* 已选择的链接 */
a:active {
  color: red;
}

</style>