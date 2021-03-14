<template>
  <div class="main">
    <div v-for="post in posts" :key="post.id">
      <router-link
        :to="{ path: `/post/${post.id}`, params: { postId: post.id } }"
      >
        <div class="post">
          <div class="post-title">
            {{ post.title }}
          </div>
          <div class="post-desc">
            <strong>摘要: </strong> <small>{{ post.body | desc }}</small>
          </div>
          <div class="post-outher">
            发表时间 {{ post.create_at | formatTime }} 阅读({{ post.reading }})
          </div>
        </div>
      </router-link>
    </div>
    <div>分页</div>
  </div>
</template>

<script>
import { getHome } from "../api/home";
export default {
  name: "Home",
  data() {
    return {
      posts: [],
      msg: 1,
      // 分页
      current: 2,
    };
  },
  methods: {
    getPosts() {
      getHome()
        .then((result) => {
          this.posts = result.data.post;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.getPosts();
  },
  filters: {
    // 正文显示指定字符
    desc: function (value) {
      if (!value) return "";
      if (value.length > 50) {
        return value.slice(0, 50) + "...";
      }
      return value;
    },

    // 格式化时间
    formatTime: function (value) {
      value = value.replace("T", " ");
      const index = value.indexOf(".");
      value = value.substring(0, index);

      return value;
    },
  },
};
</script>
<style>
/* 该组件的css样式抄袭 博客园的 */
.post {
  min-height: 10px;
  margin-bottom: 20px;
  padding-bottom: 5px;
  margin-left: 20px;
  margin-top: 1em;
  margin-right: 2em;
}

.post-title {
  font-size: 14px;
  font-weight: bold;
  padding: 0 100px 10px 20px;
  border-bottom: 1px solid #e0e0e0;
  line-height: 1.5em;
  clear: both;
  border-left: 5px solid #1fa6e6;
}

.post-desc {
  float: right;
  line-height: 1.5em;
  width: 95%;
  clear: both;
  padding: 10px 0;
}

.post-outher {
  float: none;
  clear: both;
  text-align: right;
  padding-right: 5px;
  color: #a3a3a3;
}
</style>
