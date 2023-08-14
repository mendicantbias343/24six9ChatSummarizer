// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr : true,
  devtools: { enabled: true },
  sourcemap: {
    server: true,
    client: true
  },
  css: [
    "~/assets/css/tailwind.css"
  ],
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxtjs/google-fonts',

  ],
  

  content: {
    // https://content.nuxtjs.org/api/configuration
  },
  googleFonts: {
    prefetch: true,
    families: {
      Montserrat: true,
    }
  },
 build: {
  standalone: true,
}

})
