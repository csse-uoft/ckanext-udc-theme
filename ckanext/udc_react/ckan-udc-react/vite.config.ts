import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import fixReactVirtualized from 'esbuild-plugin-react-virtualized'

// https://vitejs.dev/config/
export default defineConfig({
  base: "/udc-react",
  plugins: [react()],
  optimizeDeps: {
    include: ['@emotion/styled'],
    esbuildOptions: {
      plugins: [fixReactVirtualized],
    },
  },
  build: {
    manifest: true,
    emptyOutDir: true,
    outDir: "../public/udc-react",
    rollupOptions: {
      output: {
        manualChunks: {
          // mui: ['@mui/material'],
          // mui2: ['@mui/system', '@mui/icons-material', '@mui/base', '@emotion/react', '@emotion/styled'],
          // icons: ['@mui/icons-material'],
          // react: ['react', 'react-dom', 'react-router-dom', 'react-router'],
          markdown: ['rehype-raw', 'react-markdown'],
          codemirror: ['codemirror', '@uiw/react-codemirror', '@codemirror/lang-python', '@codemirror/lang-json'],
          datagrid: ['@mui/x-data-grid'],
        }
      }
    }
    // modulePreload: {
    //   polyfill: false
    // }
  },
})
