<template>
   <div
      class="date-navigation text-md text-primary-focus flex-row flex justify-around w-full items-stretch text-2xl sticky top-0 bg-base-100 z-20 py-3"
    >
      <div
        v-bind:class="
          previous_date
            ? 'next cursor-pointer'
            : 'next cursor-pointer grayscale'
        "
      >
        <NuxtLink v-bind:to="previous_date">⏮️</NuxtLink>
      </div>
      <div class="current-date w-4/5 text-center text-lg">
        {{ formattedDate }}
      </div>
      <div
        v-bind:class="
          next_date ? 'next cursor-pointer' : 'next cursor-pointer grayscale'
        "
      >
        <NuxtLink v-bind:to="next_date">⏭️</NuxtLink>
      </div>
    </div>
</template>

<script setup>
   const props = defineProps({
     next_date:String,
     previous_date:String,
     formattedDate:String
   })
</script>

<style lang="scss" scoped>

</style>