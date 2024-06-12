import {defineConfig} from "umi";
const { resolve } = require('path');

export default defineConfig({
  dva: {},
  title: 'Writer.AI',
  links: [
    {rel: 'shortcut icon', href: '/favicon.svg'}
  ],
  routes: [
    {
      path: "/",
      component: "@/layouts/BasicLayout"
    }
  ],
  alias: {
    //'aird': resolve(__dirname, 'node_modules/air-design/lib'),
    'aird': resolve(__dirname, 'src/components/air-design'),
  },
  base: "/",
  outputPath: "../static",
});