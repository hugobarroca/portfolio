<script lang="ts">
	import { resolve } from '$app/paths';
	import { page } from '$app/state';

	const notFound = $derived(page.status === 404);
</script>

<svelte:head>
	<title>{page.status} · Hugo Barroca</title>
	<meta name="robots" content="noindex" />
</svelte:head>

<main>
	<p>
		<span class="accent">hugo@barroca</span><span class="muted">:~$</span>
		cd {page.url.pathname}
	</p>
	{#if notFound}
		<p class="error">bash: cd: {page.url.pathname}: No such file or directory</p>
	{:else}
		<p class="error">error {page.status}: {page.error?.message}</p>
	{/if}
	<p class="status muted">exit {page.status}</p>
	<p>
		<span class="accent">hugo@barroca</span><span class="muted">:~$</span>
		<a href={resolve('/')}>cd ~</a>
	</p>
</main>

<style lang="scss">
	main {
		max-width: var(--measure);
		margin: 0 auto;
		padding: 4.5rem 1rem;
		font-size: 0.875rem;
		overflow-wrap: anywhere;

		p + p {
			margin-top: 0.25rem;
		}
	}

	.accent {
		color: var(--accent);
	}

	.muted {
		color: var(--muted);
	}

	.status {
		margin-bottom: 1.5rem;
	}
</style>
