<template>
  <div>
    <b-alert variant="success" show dismissible @dismissed="resetAlert">{{message}}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message'],
  methods: {
    resetAlert() {
      this.$emit('reset-alert');
    },
  },
};
</script>
