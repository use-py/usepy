import { defineConfig } from 'vitepress'
import { withPwa } from '@vite-pwa/vitepress'
import {
  contributing,
  font,
  github,
  ogImage,
  ogUrl,
  releases,
  vitestDescription, vitestName,
} from './meta'
import { pwa } from './scripts/pwa'
import { transformHead } from './scripts/transformHead'

export default withPwa(defineConfig({
  lang: 'en-US',
  title: vitestName,
  description: vitestDescription,
  head: [
    ['meta', { name: 'theme-color', content: '#729b1a' }],
    ['link', { rel: 'icon', href: '/logo.svg', type: 'image/svg+xml' }],
    ['link', { rel: 'alternate icon', href: '/favicon.ico', type: 'image/png', sizes: '16x16' }],
    ['meta', { name: 'keywords', content: 'vitest, vite, test, coverage, snapshot, react, vue, preact, svelte, solid, lit, ruby, cypress, puppeteer, jsdom, happy-dom, test-runner, jest, typescript, esm, tinypool, tinyspy, c8, node' }],
    ['meta', { property: 'og:title', content: vitestName }],
    ['meta', { property: 'og:description', content: vitestDescription }],
    ['meta', { property: 'og:url', content: ogUrl }],
    ['meta', { property: 'og:image', content: ogImage }],
    ['meta', { name: 'twitter:title', content: vitestName }],
    ['meta', { name: 'twitter:description', content: vitestDescription }],
    ['meta', { name: 'twitter:image', content: ogImage }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['link', { rel: 'preload', as: 'style', onload: 'this.onload=null;this.rel=\'stylesheet\'', href: font }],
    ['noscript', {}, `<link rel="stylesheet" crossorigin="anonymous" href="${font}" />`],
    ['link', { rel: 'mask-icon', href: '/logo.svg', color: '#ffffff' }],
    ['link', { rel: 'apple-touch-icon', href: '/apple-touch-icon.png', sizes: '180x180' }],
  ],
  lastUpdated: true,
  markdown: {
    theme: {
      light: 'vitesse-light',
      dark: 'vitesse-dark',
    },
  },
  themeConfig: {
    logo: '/logo.png',

    editLink: {
      pattern: 'https://github.com/mic1on/usepy/tree/main/docs/:path',
      text: '对此页面提出更改建议',
    },

    algolia: {
      appId: 'C5EHDO5QDI',
      apiKey: '2cda99c532ecbfbdeb963ece5c32967f',
      indexName: 'usepy',
      // searchParameters: {
      //   facetFilters: ['tags:en'],
      // },
    },

    socialLinks: [
      { icon: 'github', link: github },
    ],

    footer: {
      message: 'Released under the MIT License. Based on Vitest.',
      copyright: 'Copyright © 2023 MicLon',
    },

    nav: [
      { text: '指南', link: '/guide/' },
      { text: 'API', link: '/api/' },
    ],

    sidebar: {
      '/': [
        {
          text: '指南',
          items: [
            {
              text: '快速开始',
              link: '/guide/',
            }
          ],
        },
        {
          text: 'API',
          items: [
            {
              text: 'Data',
              link: '/api/',
            },
            {
              text: 'Decorator',
              link: '/api/decorator',
            },
          ],
        }
      ],
    },
  },
  pwa,
  transformHead,
}))
