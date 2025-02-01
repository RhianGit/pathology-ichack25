<template>
    <button :class="buttonClass" @click="handleClick">
        <FontAwesomeIcon v-if="icon" :icon="icon" class="button-icon" />

        <slot />
    </button>
</template>
  
<script>
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

export default {
name: 'Button',
    props: {
        type: {
            type: String,
            default: 'button'
        },
        buttonClass: {
            type: String,
            default: ''
        },
        icon: Object 
    },
    methods: {
        handleClick(event) {
            this.$emit('click', event);
        }
    }
};

</script>

<style scoped>
.icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  background: url('/icon.svg') no-repeat center center;
  background-size: contain;
  border: none;
  cursor: pointer;
}
</style>