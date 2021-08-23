<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App'
}
</script>

<style  lang="scss">
@import "./assets/css/weiqinl.lib.css";
* {
  margin: 0;
  padding: 0;
  list-style: none;
  font-size: 14px;
}
html,
body {
  height: 100%;
}
#app {
  height: 100%;
}
.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
</style>
