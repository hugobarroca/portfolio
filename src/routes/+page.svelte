<script lang="ts">
	import { onMount } from 'svelte';

	const year = new Date().getFullYear();

	const site = 'https://hugobarroca.dev';
	const title = 'Hugo Barroca · Software Developer';
	const description = 'Hugo Barroca, full-stack developer working with C#, .NET and Azure.';

	const nav = [
		{ id: 'experience', label: 'experience' },
		{ id: 'certifications', label: 'certs' },
		{ id: 'projects', label: 'projects' },
		{ id: 'hobbies', label: 'hobbies' }
	];

	// Shown under the intro. Email and LinkedIn go here once Hugo has picked them.
	const links = [
		{ label: 'github/hugobarroca', href: 'https://github.com/hugobarroca' },
		{ label: 'x/TheCodeRex', href: 'https://x.com/TheCodeRex' }
	];

	const careerStart = 2020;

	const stack = ['C#', '.NET', 'TypeScript', 'React', 'Svelte', 'Azure'];

	const projects = [
		{
			name: 'Kanju',
			status: 'live',
			href: 'https://kanju.hugobarroca.dev',
			linkLabel: 'kanju.hugobarroca.dev',
			text: [
				'A web app for Mandarin learners that answers one question: what do I need to learn to watch this show? Import the words you know from Anki, drop in a show’s subtitles, and it shows how much of each episode you’d understand and which words to learn first.',
				'It also drafts flashcards from the show’s own sentences and tracks your progress. Everything runs in the browser, with no account and nothing sent to a server.'
			],
			tags: ['TypeScript', 'Preact', 'IndexedDB', 'Cloudflare Workers']
		}
	];

	// The two frames of the classic crab invader; the hero alternates them.
	const invaderFrames = [
		[
			'..X.....X..',
			'...X...X...',
			'..XXXXXXX..',
			'.XX.XXX.XX.',
			'XXXXXXXXXXX',
			'X.XXXXXXX.X',
			'X.X.....X.X',
			'...XX.XX...'
		],
		[
			'..X.....X..',
			'X..X...X..X',
			'X.XXXXXXX.X',
			'XXX.XXX.XXX',
			'XXXXXXXXXXX',
			'.XXXXXXXXX.',
			'..X.....X..',
			'.X.......X.'
		]
	].map((frame) => frame.map((row) => [...row]));

	let current = $state('');

	// Highlight the nav link of the last section whose top has passed 30% of the screen,
	// or the last section once the page is scrolled to the bottom.
	onMount(() => {
		const sections = [...document.querySelectorAll<HTMLElement>('main section[id]')];
		const update = () => {
			const atBottom =
				window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4;
			const line = window.innerHeight * 0.3;
			const passed = atBottom
				? sections
				: sections.filter((s) => s.getBoundingClientRect().top <= line);
			current = passed.at(-1)?.id ?? '';
		};
		update();
		window.addEventListener('scroll', update, { passive: true });
		window.addEventListener('resize', update);
		return () => {
			window.removeEventListener('scroll', update);
			window.removeEventListener('resize', update);
		};
	});
</script>

<svelte:head>
	<title>{title}</title>
	<meta name="description" content={description} />
	<link rel="canonical" href="{site}/" />
	<meta property="og:type" content="website" />
	<meta property="og:site_name" content="Hugo Barroca" />
	<meta property="og:url" content="{site}/" />
	<meta property="og:title" content={title} />
	<meta property="og:description" content={description} />
	<meta property="og:image" content="{site}/og.png" />
	<meta property="og:image:width" content="1200" />
	<meta property="og:image:height" content="630" />
	<meta
		property="og:image:alt"
		content="Hugo Barroca, software developer, with a pixel crab invader"
	/>
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:creator" content="@TheCodeRex" />
</svelte:head>

<header class="topbar">
	<div class="topbar-inner">
		<a class="home" href="#top" aria-label="Back to top">
			<span class="accent">hugo@barroca</span><span class="muted">:~$</span>
		</a>
		<nav aria-label="Sections">
			<ul>
				{#each nav as item (item.id)}
					<li>
						<a href="#{item.id}" aria-current={current === item.id ? 'location' : undefined}
							>{item.label}</a
						>
					</li>
				{/each}
			</ul>
		</nav>
	</div>
</header>

<main id="top">
	<section class="hero" aria-labelledby="name">
		<p class="command" aria-hidden="true">
			<span class="accent">hugo@barroca</span><span class="muted">:~$</span>
			<span class="typed">whoami</span><span class="caret"></span>
		</p>

		<div class="hero-body">
			<div class="hero-text">
				<h1 id="name">Hugo Barroca</h1>
				<p class="role">
					Software developer <span class="sep">/</span> C# &amp; .NET <span class="sep">/</span> Azure
				</p>
				<p class="intro">
					I build back-end services in C# and .NET, run them on Azure, and write the TypeScript
					front ends that sit on top. In my own time I build tools for the things I'm learning.
				</p>
				<ul class="links">
					{#each links as link (link.href)}
						<li><a href={link.href} rel="external">{link.label}</a></li>
					{/each}
				</ul>
			</div>
			<svg class="invader" viewBox="0 0 11 8" aria-hidden="true" shape-rendering="crispEdges">
				{#each invaderFrames as frame, f (f)}
					<g class="frame frame-{f}">
						{#each frame as row, y (y)}
							{#each row as cell, x (x)}
								{#if cell === 'X'}<rect {x} {y} width="1" height="1" />{/if}
							{/each}
						{/each}
					</g>
				{/each}
			</svg>
		</div>
	</section>

	<section id="experience" aria-labelledby="experience-title">
		<h2 id="experience-title"><span class="index">01</span>experience</h2>
		<div class="body">
			<p>
				Full-stack developer since {careerStart}, mostly on the back end in C# and .NET. On the
				front end I work in TypeScript, with React or Svelte.
			</p>
			<p>
				I've built and maintained Web APIs that serve millions of requests, authentication servers
				with OAuth and OpenID Connect, and services deployed both on Azure and on-prem, backed by
				databases with many millions of rows.
			</p>
			<ul class="tags" aria-label="Stack">
				{#each stack as tag (tag)}
					<li>{tag}</li>
				{/each}
			</ul>
		</div>
	</section>

	<section id="certifications" aria-labelledby="certifications-title">
		<h2 id="certifications-title"><span class="index">02</span>certifications</h2>
		<ul class="body checklist">
			<li>
				<span class="box done" aria-hidden="true">[x]</span>
				<span>Azure Developer Associate <span class="muted">(AZ-204)</span></span>
			</li>
			<li>
				<span class="box" aria-hidden="true">[ ]</span>
				<span>Azure DevOps Engineer Expert <span class="muted">(studying)</span></span>
			</li>
		</ul>
	</section>

	<section id="projects" aria-labelledby="projects-title">
		<h2 id="projects-title"><span class="index">03</span>projects</h2>
		<div class="body">
			{#each projects as project (project.name)}
				<article class="project">
					<h3>{project.name} <span class="status">{project.status}</span></h3>
					{#each project.text as paragraph, i (i)}
						<p>{paragraph}</p>
					{/each}
					<ul class="tags" aria-label="Built with">
						{#each project.tags as tag (tag)}
							<li>{tag}</li>
						{/each}
					</ul>
					<p class="project-link"><a href={project.href} rel="external">{project.linkLabel}</a></p>
				</article>
			{/each}
		</div>
	</section>

	<section id="hobbies" aria-labelledby="hobbies-title">
		<h2 id="hobbies-title"><span class="index">04</span>hobbies</h2>
		<dl class="body hobbies">
			<div>
				<dt>bouldering</dt>
				<dd>
					Away from the keyboard I go bouldering. It's hard physical work, and every route is a
					puzzle to solve.
				</dd>
			</div>
			<div>
				<dt>animals</dt>
				<dd>
					I like animals of every kind: domestic, wild and extinct. My dog Eddie is the biggest,
					cutest thing.
				</dd>
			</div>
		</dl>
	</section>
</main>

<footer>
	<div class="footer-inner">
		<p class="command" aria-hidden="true">
			<span class="accent">hugo@barroca</span><span class="muted">:~$</span>
			<span class="caret idle"></span>
		</p>
		<p class="muted">© {year} Hugo Barroca</p>
	</div>
</footer>

<style lang="scss">
	.accent {
		color: var(--accent);
	}

	.muted {
		color: var(--muted);
	}

	/* ===== Top bar ===== */

	.topbar {
		position: sticky;
		top: 0;
		z-index: 10;
		background: var(--bg-overlay);
		backdrop-filter: blur(8px);
		-webkit-backdrop-filter: blur(8px);
		border-bottom: 1px solid var(--border);
	}

	.topbar-inner {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 1rem;
		max-width: var(--measure);
		height: var(--header-height);
		margin: 0 auto;
		padding: 0 1rem;
		font-size: 0.8125rem;
	}

	.home {
		display: none;
		text-decoration: none;
	}

	nav ul {
		display: flex;
		gap: 1rem;
	}

	nav a {
		color: var(--muted);
		text-decoration: none;

		&:hover,
		&[aria-current] {
			color: var(--accent);
		}
	}

	/* ===== Layout ===== */

	main,
	footer {
		max-width: var(--measure);
		margin: 0 auto;
		padding: 0 1rem;
	}

	section {
		padding: 3rem 0;
		scroll-margin-top: var(--header-height);
	}

	section + section {
		border-top: 1px dashed var(--border);
	}

	h2 {
		display: flex;
		align-items: baseline;
		gap: 0.75rem;
		margin-bottom: 1.25rem;
		color: var(--accent);
		font-size: 0.875rem;
		font-weight: 500;
		letter-spacing: 0.04em;
	}

	.index {
		color: var(--muted);
		font-weight: 400;
	}

	.body > * + * {
		margin-top: 1rem;
	}

	/* ===== Hero ===== */

	.hero {
		padding-top: 2.5rem;
	}

	.command {
		margin-bottom: 1.75rem;
		color: var(--text);
		font-size: 0.875rem;
		white-space: nowrap;
	}

	.typed {
		display: inline-block;
		width: 6ch;
		overflow: hidden;
		vertical-align: bottom;
		animation: type 0.5s steps(6) 0.3s both;
	}

	.caret {
		display: inline-block;
		width: 0.55em;
		height: 1.1em;
		margin-left: 0.15em;
		vertical-align: -0.15em;
		background: var(--accent);
		animation: blink 1s steps(1) 0.8s 3 forwards;
	}

	.caret.idle {
		margin-left: 0.5em;
		animation: blink 1s steps(1) infinite;
	}

	.hero-body {
		display: flex;
		flex-direction: column-reverse;
		gap: 1.5rem;
	}

	h1 {
		color: var(--text);
		font-size: clamp(2rem, 8vw, 3rem);
		font-weight: 700;
		line-height: 1.1;
		letter-spacing: -0.02em;
	}

	.role {
		margin-top: 0.5rem;
		color: var(--accent);
	}

	.sep {
		color: var(--accent-dim);
	}

	.intro {
		max-width: 34rem;
		margin-top: 1.25rem;
	}

	.links {
		display: flex;
		flex-wrap: wrap;
		gap: 0.5rem 1.5rem;
		margin-top: 1.5rem;
		font-size: 0.875rem;

		a::before {
			content: '→ ';
			color: var(--muted);
		}
	}

	.invader {
		display: none;
		width: 8.25rem;
		margin-top: 0.75rem;
		fill: var(--accent-dim);
		flex-shrink: 0;
	}

	.frame {
		animation: march 1.6s steps(1) infinite;
	}

	.frame-1 {
		visibility: hidden;
		animation-delay: -0.8s;
	}

	/* ===== Sections ===== */

	.tags {
		display: flex;
		flex-wrap: wrap;
		gap: 0.5rem;
		padding-top: 0.5rem;

		li {
			padding: 0.1rem 0.6rem;
			border: 1px solid var(--border);
			border-radius: 3px;
			background: var(--surface);
			color: var(--muted);
			font-size: 0.8125rem;
		}
	}

	.checklist li {
		display: flex;
		gap: 0.75rem;
	}

	.box {
		flex-shrink: 0;
		color: var(--muted);

		&.done {
			color: var(--accent);
		}
	}

	.project {
		padding: 1.25rem;
		border: 1px solid var(--border);
		border-radius: 4px;
		background: var(--surface);

		p,
		.tags {
			margin-top: 0.75rem;
		}

		.project-link {
			font-size: 0.875rem;

			a::before {
				content: '→ ';
				color: var(--muted);
			}
		}
	}

	h3 {
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		gap: 0.25rem 0.75rem;
		font-size: 1rem;
		font-weight: 500;
	}

	.status {
		padding: 0 0.5rem;
		border: 1px solid var(--accent-dim);
		border-radius: 3px;
		color: var(--accent);
		font-size: 0.75rem;
		font-weight: 400;
	}

	.hobbies {
		display: grid;
		gap: 1.5rem;

		> * + * {
			margin-top: 0;
		}
	}

	dt {
		color: var(--text);
		font-weight: 500;

		&::before {
			content: '# ';
			color: var(--accent-dim);
		}
	}

	dd {
		margin-top: 0.25rem;
		color: var(--text);
	}

	/* ===== Footer ===== */

	.footer-inner {
		padding: 2rem 0 3rem;
		border-top: 1px solid var(--border);
		font-size: 0.8125rem;

		.command {
			margin-bottom: 0.5rem;
		}
	}

	/* ===== Animations ===== */

	@keyframes type {
		from {
			width: 0;
		}
	}

	@keyframes march {
		0% {
			visibility: visible;
		}
		50%,
		100% {
			visibility: hidden;
		}
	}

	@keyframes blink {
		50% {
			opacity: 0;
		}
		to {
			opacity: 0;
		}
	}

	/* ===== Wider screens ===== */

	@media (min-width: 640px) {
		.home {
			display: inline;
		}

		nav ul {
			gap: 1.25rem;
		}

		nav a::before {
			content: './';
			color: var(--accent-dim);
		}

		.hero {
			padding-top: 4.5rem;
			padding-bottom: 4rem;
		}

		.hero-body {
			flex-direction: row;
			align-items: flex-start;
			justify-content: space-between;
			gap: 2.5rem;
		}

		.invader {
			display: block;
		}

		.hobbies {
			grid-template-columns: 1fr 1fr;
			gap: 2rem;
		}
	}
</style>
