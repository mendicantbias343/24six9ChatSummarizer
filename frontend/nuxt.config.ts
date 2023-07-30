// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: false },
  css: [
    "~/assets/css/tailwind.css"
  ],
  modules: [
    '@nuxt/content',
    '@nuxtjs/tailwindcss',
    '@nuxtjs/google-fonts',

  ],
  buildModules: ['@nuxt/content'],

  content: {
    // https://content.nuxtjs.org/api/configuration
  },
  googleFonts: {
    prefetch: true,
    families: {
      Montserrat: true,
    }
  }
})
