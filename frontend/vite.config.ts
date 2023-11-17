import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from "path";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
      host: true, // needed for the Docker Container port mapping to work
      strictPort: true, // not necessary
      port: 3000, // you can replace this port with any port
      open: false,
      watch: {
          usePolling: true,
      },
  },
  resolve: {
      alias: {
          "@": path.resolve(__dirname, "src"),
      },
  },
});
