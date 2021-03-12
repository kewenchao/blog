<template>
  <div class="main">
    <div v-for="tag in tags" :key="tag.id">
      {{tag.name}}
    </div>
  </div>
</template>

<script>
import request from '../network/request'
export default {
    name: "Category",
    data() {
      return {
        tags:[]
        }
    },
    methods: {
      getTag(){
        request({
          url: "/category"
        }).then((result) => {
          this.tags = result.data.category
        }).catch((err) => {
          console.log(err)
        });
      }
    },
    created(){
      this.getTag()
    }
}
</script>

<style>

</style>