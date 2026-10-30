import adapter from '@sveltejs/adapter-cloudflare';
import { sveltekit } from '@sveltejs/kit/vite';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import { defineConfig } from 'vite';

// The Cloudflare Pages build image sets NODE_OPTIONS=--use-openssl-ca. SvelteKit runs part of
// the build in a worker thread that copies process.env, and Node 20 rejects that flag there
// (not yet checked on the Node 22 of the v3 build image, so the strip stays).
if (process.env.NODE_OPTIONS?.includes('--use-openssl-ca')) {
	process.env.NODE_OPTIONS = process.env.NODE_OPTIONS.replace('--use-openssl-ca', '').trim();
}

export default defineConfig({
	plugins: [
		sveltekit({
			adapter: adapter(),
			preprocess: vitePreprocess()
		})
	]
});
