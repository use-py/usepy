import { defineConfig } from 'vitepress'
import type { DefaultTheme } from 'vitepress/types/default-theme'
import { withPwa } from '@vite-pwa/vitepress'
import {
  font,
  github,
  blog,
  ogImage,
  ogUrl,
  vitestDescription, vitestName,
} from './meta'
import { pwa } from './scripts/pwa'
import { transformHead } from './scripts/transformHead'

interface SidebarItem extends DefaultTheme.SidebarItem {
  tags?: string[]
}

export default withPwa(defineConfig({
  lang: 'zh-CN',
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
    theme: 'vitesse-dark',
  },
  themeConfig: {
    logo: '/logo.png',

    editLink: {
      pattern: 'https://github.com/mic1on/usepy/tree/main/docs/:path',
      text: '对此页面提出更改建议',
    },

    algolia: {
      appId: 'YEWHQHLU31',
      apiKey: 'bb61897ed96af7fc93af57f7e2106623',
      indexName: 'usepy-52caiji',
      // searchParameters: {
      //   facetFilters: ['tags:en'],
      // },
    },

    socialLinks: [
      { icon: 'github', link: github },
      {
        icon: {
          svg: '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 512 512"><path fill="currentColor" d="M172.2 226.8c-14.6-2.9-28.2 8.9-28.2 23.8V301c0 10.2 7.1 18.4 16.7 22c18.2 6.8 31.3 24.4 31.3 45c0 26.5-21.5 48-48 48s-48-21.5-48-48V120c0-13.3-10.7-24-24-24H24c-13.3 0-24 10.7-24 24v248c0 89.5 82.1 160.2 175 140.7c54.4-11.4 98.3-55.4 109.7-109.7c17.4-82.9-37-157.2-112.5-172.2zM209 0c-9.2-.5-17 6.8-17 16v31.6c0 8.5 6.6 15.5 15 15.9c129.4 7 233.4 112 240.9 241.5c.5 8.4 7.5 15 15.9 15h32.1c9.2 0 16.5-7.8 16-17C503.4 139.8 372.2 8.6 209 0zm.3 96c-9.3-.7-17.3 6.7-17.3 16.1v32.1c0 8.4 6.5 15.3 14.8 15.9c76.8 6.3 138 68.2 144.9 145.2c.8 8.3 7.6 14.7 15.9 14.7h32.2c9.3 0 16.8-8 16.1-17.3c-8.4-110.1-96.5-198.2-206.6-206.7z"/></svg>'
        }, link: blog
      },
    ],

    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2023 MicLon',
    },

    nav: [
      { text: '指南', link: '/guide/' },
      { text: 'API', link: '/api/' },
      { text: '插件', link: '/plugin/' },
    ],

    sidebar: {
      '/plugin': [
        {
          text: '扩展插件',
          items: [
            {
              text: 'usepy-plugin-logger',
              link: '/plugin/logger',
            },
            {
              text: 'usepy-plugin-notify',
              link: '/plugin/notify',
            }
          ],
        }
      ],
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
          text: 'Core',
          items: [
            {
              text: 'useAdDict',
              link: '/api/addict',
            },
            {
              text: 'useDict',
              link: '/api/dict',
            },
            {
              text: 'useList',
              link: '/api/list',
            },
            {
              text: 'useBloomFilter',
              link: '/api/bloom_filter',
            },
            {
              text: 'useString',
              link: '/api/string',
            },
            {
              text: 'useDateTime',
              link: '/api/datetime',
            },
            {
              text: 'usePath',
              link: '/api/path',
            },
            {
              text: 'useParser',
              link: '/api/parser',
            },
          ],
        },
        {
          text: 'Decorator',
          items: [
            {
              text: 'useThread',
              link: '/decorator/thread',
            },
            {
              text: 'useSingleton',
              link: '/decorator/singleton',
            },
            {
              text: 'useTimeIt',
              link: '/decorator/timeit',
            },
            {
              text: 'useCatchError',
              link: '/decorator/catch_error',
            },
            {
              text: 'useExceptDebug',
              link: '/decorator/except_debug',
            },
            {
              text: 'useRunInThread',
              link: '/decorator/run_in_thread',
            },
            {
              text: 'useListify',
              link: '/decorator/listify',
            },
          ],
        },
        {
          text: 'Utils',
          items: [
            {
              text: 'useTimer',
              link: '/utils/timer',
            },
            {
              text: 'useTimeout',
              link: '/utils/timeout',
            },
            {
              text: 'useBloomFilter',
              link: '/utils/bloom_filter',
            },
            {
              text: 'useIs',
              link: '/utils/is',
            },
            {
              text: 'useTo',
              link: '/utils/to',
            },
            {
              text: 'utils',
              link: '/utils/utils',
            }
          ],
        },
      ] as SidebarItem[],
    },
  },
  pwa,
  transformHead,
}))
