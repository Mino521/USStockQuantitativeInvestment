<template>
  <div class="wq-topbar">
    <el-menu router default-active="activeIndex" class="el-menu-top" mode="horizontal" @select="handleSelect">
      <h1>Company Analysis</h1>
      <div class="top-menu-item">
        <el-submenu index="sysset">
          <template slot="title">user0</template>
          <el-menu-item index="grzx-bky">ListA</el-menu-item>
          <el-menu-item index="grzx-xmdz">ListB</el-menu-item>
          <el-menu-item index="/login">Exit</el-menu-item>
        </el-submenu>
      </div>
    </el-menu>
  </div>
</template>
<script>
export default {
  data () {
    return {
      activeIndex: '1',
      moreTheme: '20a0ff',
      skinDialogVisible: false
    }
  },
  mounted () {
    let themeClassName = ''
    let localTheme = localStorage.getItem('themeValue')
    themeClassName = localTheme || '20a0ff'
    this.changeClass(document.body, 'custom-' + themeClassName)
    this.moreTheme = themeClassName
  },
  methods: {
    changeClass (element, className) {
      if (!element || !className) return
      element.className = className
    },
    handleSelect (key, keyPath) {
      console.log(key)
      console.log(keyPath)
    },
    changeTheme (themeValue) {
      this.changeClass(document.body, 'custom-' + themeValue)
      this.moreTheme = themeValue
      localStorage.setItem('themeValue', themeValue)
    }
  }
}
</script>
<style lang="scss">
.wq-topbar {
  .el-menu-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    .logo {
      line-height: 60px;
      padding: 6px;
      padding-left: 60px;
    }
    .top-menu-item {
      flex: 1;
      display: flex;
      justify-content: flex-end;
    }
  }
}
</style>
