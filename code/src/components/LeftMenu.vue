<template>
  <div class="leftmenu">
    <el-row>
      <el-col :span="24">
        <el-menu default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
          <el-menu-item-group key="index">
            <el-menu-item index="1">
              <i class="el-icon-s-home"></i>
              Home
            </el-menu-item>
          </el-menu-item-group>
          <el-submenu v-for="(item) in items" :index="item.path" :key="item.name">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>{{item.name}}</span>
            </template>
            <el-menu-item-group v-for="citem in item.children" :key="citem.name">
              <el-menu-item :index="citem.path">{{citem.name}}</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'LeftMenu',
  data () {
    return {
      items: [
        {
          icon: 'fa-money',
          name: 'select',
          path: 'found',
          children: [
            {
              name: 'children',
              path: 'found1',
            }, {
              name: 'children2',
              path: 'found2',
            },
          ]
        }, {
          icon: 'fa-money',
          name: 'userManager',
          path: 'user',
          children: [
            {
              name: 'children',
              path: 'found3',
            }, {
              name: 'children',
              path: 'found4',
            },
          ]
        }
      ]
    }
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>
<style lang="less" scoped>
.leftmenu{
  .el-menu{
    min-height: 92vh;
  }
}
</style>