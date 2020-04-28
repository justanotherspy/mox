<template>
  <div id="doll">
      <!-- setup doll card visuals here -->
      <!-- bind elements to data inherited from parent component app -->
      <h2>Name: {{ name }}</h2>
      <h2>Description: {{ description }}</h2>
      <h2>Image: {{ name + '.jpg'}}</h2>
      <h2>Scanned: {{ scannedDate }}</h2>
  </div>
</template>

<script>
export default {
  name: 'DollCard',
  props: {
    name: String,
    description: String,
    scannedDate: String
  }
}
</script>

<style>

</style>
