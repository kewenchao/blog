<template>
  <div class="main">
    <div v-for="post in posts" :key="post.id">
      <div class="post">
        {{post.title}}
        <div class="des">
          <!-- 阅读量 -->
        <i class="el-icon-view"></i> {{post.reading}}
        <!-- 创建时间 -->
        <i class="el-icon-date"></i>
        
          {{post.create_at}}

        <!-- 评论 -->
        <i class="el-icon-chat-dot-round"></i>
        1
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import request from "../network/request";
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
      request({
        url: "/post",
        params: {
          limit: 100,
          page: 1,
        },
      })
        .then((result) => {
          this.posts = result.data.post;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    look(){
      // 查看文章详情
    }
  },
  created() {
    this.getPosts();
  },
  filters: {
    // 正文显示指定字符
    desc: function (value) {
      if (!value) return "";
      if (value.length > 21) {
        return value.slice(0, 21) + "...";
      }
      return value;
    },
  },
};
</script>
<style>
.post
{
    color: red;
    background-color: aliceblue;
    line-height: normal;
    font-size: 20px;
}

</style>
