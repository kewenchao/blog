<template>
  <a-layout id="components-layout-demo-top" class="layout">
    <a-layout-header>
      <div class="logo" />
      <a-menu
        theme="dark"
        mode="horizontal"
        :default-selected-keys="['1']"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="1">
          <router-link to="/">首页</router-link>
        </a-menu-item>
        <a-menu-item key="2">
          <router-link to="/category">分类</router-link>
        </a-menu-item>
        <a-menu-item key="3"> 简历 </a-menu-item>
        <a-menu-item key="4"> 开源项目 </a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout-content style="padding: 0 50px">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>Home</a-breadcrumb-item>
        <a-breadcrumb-item>List</a-breadcrumb-item>
        <a-breadcrumb-item>App</a-breadcrumb-item>
      </a-breadcrumb>
      <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">
        {{ posts }}
        {{ msg }}
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      zy7y Blog ©2021 Created by Ant UED
    </a-layout-footer>
  </a-layout>
</template>

<script>
import request from "../network/request";
export default {
  name: "Main",
  data() {
    return {
      posts: [],
      msg: 1,
    };
  },
  methods: {
    getPosts() {
      request({
        url: "/post",
      })
        .then((result) => {
          this.posts = result;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.getPosts();
  },
};
</script>
<style>
#components-layout-demo-top .logo {
  width: 120px;
  height: 31px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px 24px 16px 0;
  float: left;
}
</style>
