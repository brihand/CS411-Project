<template>
  <div class="index">
    <el-autocomplete popper-class="my-autocomplete" v-model="state" :fetch-suggestions="querySearch" placeholder="请输入内容" @select="handleSelect">
      <i class="el-icon-search el-input__icon" slot="suffix" @click="handleIconClick">
      </i>
      <template slot-scope="{ item }">
        <div class="name">{{ item.value }}</div>
        <span class="addr">{{ item.address }}</span>
      </template>
    </el-autocomplete>
  </div>
</template>

<script>
export default {
  data () {
    return {
      restaurants: [],
      state: ''
    };
  },
  methods: {
    querySearch (queryString, cb) {
      var restaurants = this.restaurants;
      var results = queryString ? restaurants.filter(this.createFilter(queryString)) : restaurants;
      // 调用 callback 返回建议列表的数据
      cb(results);
    },
    createFilter (queryString) {
      return (restaurant) => {
        return (restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
      };
    },
    loadAll () {
      return [
        { "value": "三全鲜食（北新泾店）", "address": "长宁区新渔路144号" },
        { "value": "Hot honey 首尔炸鸡（仙霞路）", "address": "上海市长宁区淞虹路661号" },
        { "value": "新旺角茶餐厅", "address": "上海市普陀区真北路988号创邑金沙谷6号楼113" },
      ];
    },
    handleSelect (item) {
      console.log(item);
    },
    handleIconClick (ev) {
      console.log(ev);
    }
  },
  mounted () {
    this.restaurants = this.loadAll();
  }
}
</script>
<style lang="less" scoped>
.index{
  /deep/ .el-autocomplete{
    width: 100%;
    padding: 20px;
  }
}
</style>