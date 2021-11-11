<template>
  <div class="home">
    <Head />
    <el-row>
      <el-col :span="4">
        <LeftMenu />
      </el-col>
      <el-col :span="20">
        <router-view></router-view>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Head from '../components/HeadNav.vue'
import LeftMenu from '../components/LeftMenu.vue'
export default {
  data () {
    return {

    }
  },
  methods: {
  },
  components: {
    Head,
    LeftMenu
  }
}
</script>