import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig, searchForWorkspaceRoot } from 'vite';

// The Cloudflare Pages build image sets NODE_OPTIONS=--use-openssl-ca. SvelteKit runs part of
// the build in a worker thread that copies process.env, and Node 20 rejects that flag there.
if (process.env.NODE_OPTIONS?.includes('--use-openssl-ca')) {
	process.env.NODE_OPTIONS = process.env.NODE_OPTIONS.replace('--use-openssl-ca', '').trim();
}

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		fs: {
			allow: [
				// search up for workspace root
				searchForWorkspaceRoot(process.cwd())
				// your custom rules
			]
		}
	}
});
