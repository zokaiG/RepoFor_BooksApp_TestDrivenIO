<template>
  <div>
    <b-alert :variant="variant" show dismissible @dismissed="resetAlert">{{message}}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message', 'variant'],
  methods: {
    resetAlert() {
      this.$emit('reset-alert');
    },
  },
};
</script>
