<template>
  <div id="head">
    <h1>Verified: {{ verified }}</h1>
  </div>
</template>

<script>
export default {
  name: 'HeadCard',
  props: {
    verified: Boolean
  }
}
</script>

<style>

</style>
