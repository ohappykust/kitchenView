// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: false,
  devtools: { enabled: true },
  modules: [
    "@nuxtjs/tailwindcss",
    "shadcn-nuxt",
    "@pinia/nuxt",
    "@nuxtjs/color-mode"
  ],
  app: {
    head: {
      link: [
        {rel: 'apple-touch-icon', sizes: '180x180', href: '/apple-touch-icon.png'},
        {rel: 'icon', type: 'image/png', sizes: '32x32', href: '/favicon-32x32.png'},
        {rel: 'icon', type: 'image/png', sizes: '16x16', href: '/favicon-16x16.png'},
        {rel: 'manifest', href: '/site.webmanifest'},
      ]
    }
  },
  shadcn: {
    prefix: '',
    componentDir: './components/ui'
  },
  colorMode: {
    preference: 'light',
    classSuffix: ''
  },
  tailwindcss: {
    exposeConfig: true,
    viewer: true,
    cssPath: '~/assets/css/tailwind.css'
  },
  router: {
    options: {
      linkActiveClass: "bg-border"
    }
  },
  runtimeConfig: {
    public: {
      baseURL: process.env.BASE_URL,
      staticBaseURL: process.env.STATIC_BASE_URL
    },
  },
})