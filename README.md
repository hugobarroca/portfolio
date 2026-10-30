# Portfolio

My personal site at [hugobarroca.dev](https://hugobarroca.dev): a one-page, terminal-style overview of who I am, my experience, certifications, projects and hobbies.

Built with SvelteKit 3 and Svelte 5, prerendered, and deployed to Cloudflare Pages on every push to `main`. Needs Node 22.17 or later.

## Run

```bash
npm install
npm run dev
```

## Checks

```bash
npm run check
npm run lint
npm run build
```

There are no tests.

## Link-preview image

`static/og.png` is drawn by a script (Pillow, fonts from `node_modules`):

```bash
python scripts/make_og_image.py
```
