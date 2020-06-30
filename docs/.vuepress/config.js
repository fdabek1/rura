module.exports = {
  base: '/rura/',
  title: 'Rura',
  description: 'Documentation of the Rura library',
  head: [
    ['link', {rel: 'icon', href: '/favicon.ico'}] // TODO - This doesnt work
  ],
  themeConfig: {
    docsDir: 'docs',
    nav: [
      {text: 'Home', link: '/'},
      {text: 'Usage', link: '/usage/'},
      {text: 'Components', link: '/components/'},
      {text: 'Models', link: '/models/'},
    ],
    displayAllHeaders: true,
    sidebar: {
      '/usage/': [
        'codes',
      ],
      '/components/':
        [
          {
            title: 'Data',
            collapsable: false,
            children: [
              'data/',
              'data/external',
            ]
          },
          {
            title: 'Transform',
            collapsable: false,
            children: [
              'transform/',
            ]
          },
          {
            title: 'Model',
            collapsable: false,
            children: [
              'model/',
            ]
          },
          {
            title: 'Process',
            collapsable: false,
            children: [
              'process/',
            ]
          },
          {
            title: 'Metric',
            collapsable: false,
            children: [
              'metric/',
            ]
          },
        ],
    }
  }
};