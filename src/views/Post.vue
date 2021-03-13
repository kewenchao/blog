<template>
  <div class="topics">
    <div class="post-title">{{ post.title }}</div>
    <div class="post-body">
      {{ post.body }}
      <div id="BlogPostCategory">
        <small>
          分类:
          <a href="/" style="display: inline">{{ tag.name }}</a>
        </small>
      </div>
    </div>
    <div class="post-outher">
      发表时间 {{ post.create_at | formatTime }} 阅读({{ post.reading }})
    </div>
    <div class="comment">
        <div class="c-list">评论列表</div>
        <div v-for="c in comment" :key="c.id">
            <div class="cont">#{{c.id}} - {{c.author}}@ <br>
            {{c.content}}</div>
            <div style="color: #666;">{{c.create_at | formatTime}}</div>
        </div>

    </div>
  </div>
</template>

<script>
import { getPost } from "../api/home";
export default {
  name: "Post",
  data() {
    return {
      postId: this.$route.params.id,
      post: {},
      tag: {},
      comment: [],
    };
  },
  methods: {
    detail: function () {
      getPost(this.postId)
        .then((result) => {
          console.log(result);
          this.post = result.data.post;
          this.tag = result.data.category;
          this.comment = result.data.comment;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    console.log(this.$route.params);
    this.detail();
  },
  filters: {
    // 格式化时间
    formatTime: function (value) {
      value = value.replace("T", " ");
      const index = value.indexOf(".");
      value = value.slice(0, index);

      return value;
    },
  },
};
</script>

<style>
.topics {
  min-height: 200px;
  padding: 1em;
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

.post-body {
  padding: 5px 2px 5px 5px;
  line-height: 1.8;
  color: #000;
  border-bottom: 1px solid #000;
}

.post-outher {
  float: none;
  clear: both;
  text-align: right;
  padding-right: 5px;
  color: #a3a3a3;
}

#BlogPostCategory {
  margin-bottom: 10px;
}

.c-list{
    font-weight: bold;
    border-bottom: 1px solid #333;
    font-size: 1.2em;
    margin-top: 20px;
    /* margin: 20px 10px 0; */
    padding: 0 0 5px 8px;
}

.cont{
        border-bottom: 1px solid #ccc;
    /* background: url(images/comment.gif) no-repeat 5px 0; */
    padding: 15px 0 10px 40px;
    min-height: 35px;
    _height: 35px;
    margin-bottom: 1em;
    line-height: 1.5em;
    margin-right: 10px;
}
</style>