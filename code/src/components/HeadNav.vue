<template>
  <div class="head">
    <div class="d-flex justify-content-between">
      <div class="left">ServerManager</div>
      <div class="right">
        <el-dropdown>
          <span class="el-dropdown-link">
            Welcome<i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>username</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>
<style lang="less" scoped>
.head{
  background-color:#324057;
  color: #fff;
  padding: 20px;
  .right{
    span{
      color: #fff;
    }
  }
}
</style>