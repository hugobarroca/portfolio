<script lang="ts">
	import '../app.css';
	import { onMount } from 'svelte';
	import githubLogo from '/static/icons/github-mark-white.svg';
	import xLogo from '/static/icons/x-logo-white.svg';
	import profilePhoto from '/static/Me.jpg';

	let typedText = '';
	let showMainContent = false;

	const lines = ['Hey!', 'My name is Hugo Barroca', 'I am a <Software Developer />'];
	const typeSpeed = 55;
	const deleteSpeed = 30;
	const pauseBetween = 800;
	const pauseBeforeDelete = 600;

	async function sleep(ms: number) {
		return new Promise((resolve) => setTimeout(resolve, ms));
	}

	async function typewriterSequence() {
		for (let i = 0; i < lines.length; i++) {
			const line = lines[i];
			// Type out the line
			for (let j = 0; j <= line.length; j++) {
				typedText = line.slice(0, j);
				await sleep(typeSpeed);
			}

			// If it's the last line, keep it and reveal content
			if (i === lines.length - 1) {
				await sleep(pauseBetween);
				showMainContent = true;
				break;
			}

			// Pause, then delete
			await sleep(pauseBeforeDelete);
			for (let j = line.length; j >= 0; j--) {
				typedText = line.slice(0, j);
				await sleep(deleteSpeed);
			}
			await sleep(pauseBetween);
		}
	}

	onMount(() => {
		typewriterSequence();
	});
</script>

<main>
	<!-- Floating space invaders background decoration -->
	<div class="invader-bg" aria-hidden="true">
		<svg class="invader invader-1" viewBox="0 0 11 8" width="30" height="22">
			<path d="M2,0 h1 v1 h-1z M8,0 h1 v1 h-1z M1,1 h1 v1 h-1z M3,1 h5 v1 h-5z M9,1 h1 v1 h-1z M0,2 h1 v1 h-1z M2,2 h1 v1 h-1z M3,2 h5 v1 h-5z M8,2 h1 v1 h-1z M10,2 h1 v1 h-1z M0,3 h1 v1 h-1z M2,3 h7 v1 h-7z M10,3 h1 v1 h-1z M0,4 h11 v1 h-11z M1,5 h1 v1 h-1z M3,5 h1 v1 h-1z M7,5 h1 v1 h-1z M9,5 h1 v1 h-1z M0,6 h1 v1 h-1z M2,6 h1 v1 h-1z M8,6 h1 v1 h-1z M10,6 h1 v1 h-1z M2,7 h1 v1 h-1z M4,7 h1 v1 h-1z M6,7 h1 v1 h-1z M8,7 h1 v1 h-1z" fill="currentColor"/>
		</svg>
		<svg class="invader invader-2" viewBox="0 0 11 8" width="24" height="18">
			<path d="M3,0 h2 v1 h-2z M6,0 h2 v1 h-2z M0,1 h11 v1 h-11z M0,2 h1 v1 h-1z M2,2 h7 v1 h-7z M10,2 h1 v1 h-1z M0,3 h1 v1 h-1z M2,3 h1 v1 h-1z M4,3 h3 v1 h-3z M8,3 h1 v1 h-1z M10,3 h1 v1 h-1z M1,4 h9 v1 h-9z M1,5 h1 v1 h-1z M3,5 h1 v1 h-1z M7,5 h1 v1 h-1z M9,5 h1 v1 h-1z M1,6 h1 v1 h-1z M9,6 h1 v1 h-1z M0,7 h2 v1 h-2z M9,7 h2 v1 h-2z" fill="currentColor"/>
		</svg>
		<svg class="invader invader-3" viewBox="0 0 11 8" width="20" height="15">
			<path d="M2,0 h1 v1 h-1z M8,0 h1 v1 h-1z M1,1 h1 v1 h-1z M3,1 h5 v1 h-5z M9,1 h1 v1 h-1z M0,2 h1 v1 h-1z M2,2 h1 v1 h-1z M3,2 h5 v1 h-5z M8,2 h1 v1 h-1z M10,2 h1 v1 h-1z M0,3 h1 v1 h-1z M2,3 h7 v1 h-7z M10,3 h1 v1 h-1z M0,4 h11 v1 h-11z M1,5 h1 v1 h-1z M3,5 h1 v1 h-1z M7,5 h1 v1 h-1z M9,5 h1 v1 h-1z M0,6 h1 v1 h-1z M2,6 h1 v1 h-1z M8,6 h1 v1 h-1z M10,6 h1 v1 h-1z M2,7 h1 v1 h-1z M4,7 h1 v1 h-1z M6,7 h1 v1 h-1z M8,7 h1 v1 h-1z" fill="currentColor"/>
		</svg>
		<svg class="invader invader-4" viewBox="0 0 11 8" width="26" height="20">
			<path d="M3,0 h2 v1 h-2z M6,0 h2 v1 h-2z M0,1 h11 v1 h-11z M0,2 h1 v1 h-1z M2,2 h7 v1 h-7z M10,2 h1 v1 h-1z M0,3 h1 v1 h-1z M2,3 h1 v1 h-1z M4,3 h3 v1 h-3z M8,3 h1 v1 h-1z M10,3 h1 v1 h-1z M1,4 h9 v1 h-9z M1,5 h1 v1 h-1z M3,5 h1 v1 h-1z M7,5 h1 v1 h-1z M9,5 h1 v1 h-1z M1,6 h1 v1 h-1z M9,6 h1 v1 h-1z M0,7 h2 v1 h-2z M9,7 h2 v1 h-2z" fill="currentColor"/>
		</svg>
		<svg class="invader invader-5" viewBox="0 0 11 8" width="18" height="14">
			<path d="M2,0 h1 v1 h-1z M8,0 h1 v1 h-1z M1,1 h1 v1 h-1z M3,1 h5 v1 h-5z M9,1 h1 v1 h-1z M0,2 h1 v1 h-1z M2,2 h1 v1 h-1z M3,2 h5 v1 h-5z M8,2 h1 v1 h-1z M10,2 h1 v1 h-1z M0,3 h1 v1 h-1z M2,3 h7 v1 h-7z M10,3 h1 v1 h-1z M0,4 h11 v1 h-11z M1,5 h1 v1 h-1z M3,5 h1 v1 h-1z M7,5 h1 v1 h-1z M9,5 h1 v1 h-1z M0,6 h1 v1 h-1z M2,6 h1 v1 h-1z M8,6 h1 v1 h-1z M10,6 h1 v1 h-1z M2,7 h1 v1 h-1z M4,7 h1 v1 h-1z M6,7 h1 v1 h-1z M8,7 h1 v1 h-1z" fill="currentColor"/>
		</svg>
		<svg class="invader invader-6" viewBox="0 0 11 8" width="22" height="16">
			<path d="M3,0 h2 v1 h-2z M6,0 h2 v1 h-2z M0,1 h11 v1 h-11z M0,2 h1 v1 h-1z M2,2 h7 v1 h-7z M10,2 h1 v1 h-1z M0,3 h1 v1 h-1z M2,3 h1 v1 h-1z M4,3 h3 v1 h-3z M8,3 h1 v1 h-1z M10,3 h1 v1 h-1z M1,4 h9 v1 h-9z M1,5 h1 v1 h-1z M3,5 h1 v1 h-1z M7,5 h1 v1 h-1z M9,5 h1 v1 h-1z M1,6 h1 v1 h-1z M9,6 h1 v1 h-1z M0,7 h2 v1 h-2z M9,7 h2 v1 h-2z" fill="currentColor"/>
		</svg>
	</div>

	<!-- Terminal header -->
	<div class="header">
		<div class="terminal-bar">
			<div class="terminal-dots">
				<span class="dot dot-red"></span>
				<span class="dot dot-yellow"></span>
				<span class="dot dot-green"></span>
			</div>
			<span class="terminal-title">hugo@portfolio:~</span>
		</div>
		<div class="intro-text flex-center">
			<div class="fake-code-container">
				<span class="prompt-symbol">&gt;&nbsp;</span>
				<span class="cursor">
					<h3 class="secondary-header">{typedText}</h3>
				</span>
			</div>
		</div>
	</div>

	<!-- Wave divider -->
	<div class="container">
		<svg viewBox="0 0 500 500" preserveAspectRatio="xMinYMin meet">
			<path class="wave" d="M0,0 C150,120 350,-30 500,20 L500,00 L0,0 Z"></path>
		</svg>
	</div>

	<!-- Main content -->
	{#if showMainContent}
	<div class="general-container">
		<div class="main-content">

			<!-- About Me -->
			<section class="section-card">
				<div class="section-header">
					<svg class="section-invader" viewBox="0 0 11 8" width="28" height="20">
						<path d="M2,0 h1 v1 h-1z M8,0 h1 v1 h-1z M1,1 h1 v1 h-1z M3,1 h5 v1 h-5z M9,1 h1 v1 h-1z M0,2 h1 v1 h-1z M2,2 h1 v1 h-1z M3,2 h5 v1 h-5z M8,2 h1 v1 h-1z M10,2 h1 v1 h-1z M0,3 h1 v1 h-1z M2,3 h7 v1 h-7z M10,3 h1 v1 h-1z M0,4 h11 v1 h-11z M1,5 h1 v1 h-1z M3,5 h1 v1 h-1z M7,5 h1 v1 h-1z M9,5 h1 v1 h-1z M0,6 h1 v1 h-1z M2,6 h1 v1 h-1z M8,6 h1 v1 h-1z M10,6 h1 v1 h-1z M2,7 h1 v1 h-1z M4,7 h1 v1 h-1z M6,7 h1 v1 h-1z M8,7 h1 v1 h-1z" fill="currentColor"/>
					</svg>
					<h2>About Me</h2>
				</div>
				<div class="intro-and-photo">
					<div class="about-text">
						<p>
							I'm a software developer with a passion for technology and innovation.
							I'm always looking for new challenges and opportunities to learn and grow!
						</p>
					</div>
					<div class="profile-picture-wrapper">
						<img class="profile-picture" src={profilePhoto} alt="Hugo Barroca" />
					</div>
				</div>
			</section>

			<!-- Experience -->
			<section class="section-card">
				<div class="section-header">
					<svg class="section-invader" viewBox="0 0 11 8" width="28" height="20">
						<path d="M3,0 h2 v1 h-2z M6,0 h2 v1 h-2z M0,1 h11 v1 h-11z M0,2 h1 v1 h-1z M2,2 h7 v1 h-7z M10,2 h1 v1 h-1z M0,3 h1 v1 h-1z M2,3 h1 v1 h-1z M4,3 h3 v1 h-3z M8,3 h1 v1 h-1z M10,3 h1 v1 h-1z M1,4 h9 v1 h-9z M1,5 h1 v1 h-1z M3,5 h1 v1 h-1z M7,5 h1 v1 h-1z M9,5 h1 v1 h-1z M1,6 h1 v1 h-1z M9,6 h1 v1 h-1z M0,7 h2 v1 h-2z M9,7 h2 v1 h-2z" fill="currentColor"/>
					</svg>
					<h2>My Experience</h2>
				</div>
				<p>
					I've been working as a fullstack developer for the past 5 years, honing my C# and .NET
					skills! I also occasionally dabble in the front end, preferring to work with TypeScript and
					either ReactJS or Svelte.
				</p>
				<p>
					During this time, I've developed and maintained Web APIs which have served millions of
					requests, authentication servers with OAuth and OpenID, I've deployed services in both Azure
					and on-prem, and worked with databases with many millions of rows of data!
				</p>
			</section>

			<!-- Certifications -->
			<section class="section-card">
				<div class="section-header">
					<svg class="section-invader" viewBox="0 0 11 8" width="28" height="20">
						<path d="M2,0 h1 v1 h-1z M8,0 h1 v1 h-1z M1,1 h1 v1 h-1z M3,1 h5 v1 h-5z M9,1 h1 v1 h-1z M0,2 h1 v1 h-1z M2,2 h1 v1 h-1z M3,2 h5 v1 h-5z M8,2 h1 v1 h-1z M10,2 h1 v1 h-1z M0,3 h1 v1 h-1z M2,3 h7 v1 h-7z M10,3 h1 v1 h-1z M0,4 h11 v1 h-11z M1,5 h1 v1 h-1z M3,5 h1 v1 h-1z M7,5 h1 v1 h-1z M9,5 h1 v1 h-1z M0,6 h1 v1 h-1z M2,6 h1 v1 h-1z M8,6 h1 v1 h-1z M10,6 h1 v1 h-1z M2,7 h1 v1 h-1z M4,7 h1 v1 h-1z M6,7 h1 v1 h-1z M8,7 h1 v1 h-1z" fill="currentColor"/>
					</svg>
					<h2>Certifications</h2>
				</div>
				<p>
					I'm certified as an Azure Developer (AZ-204), and I'm currently studying for my second
					Azure certification (DevOps Expert).
				</p>
			</section>

			<!-- Projects -->
			<section class="section-card">
				<div class="section-header">
					<svg class="section-invader" viewBox="0 0 11 8" width="28" height="20">
						<path d="M3,0 h2 v1 h-2z M6,0 h2 v1 h-2z M0,1 h11 v1 h-11z M0,2 h1 v1 h-1z M2,2 h7 v1 h-7z M10,2 h1 v1 h-1z M0,3 h1 v1 h-1z M2,3 h1 v1 h-1z M4,3 h3 v1 h-3z M8,3 h1 v1 h-1z M10,3 h1 v1 h-1z M1,4 h9 v1 h-9z M1,5 h1 v1 h-1z M3,5 h1 v1 h-1z M7,5 h1 v1 h-1z M9,5 h1 v1 h-1z M1,6 h1 v1 h-1z M9,6 h1 v1 h-1z M0,7 h2 v1 h-2z M9,7 h2 v1 h-2z" fill="currentColor"/>
					</svg>
					<h2>My Projects</h2>
				</div>
				<p>
					I'm currently working on a Chrome extension to help redirect you away from distracting
					sites! It's a work in progress, so I'll update you soon.
				</p>
			</section>

			<!-- Hobbies -->
			<section class="section-card">
				<div class="section-header">
					<svg class="section-invader" viewBox="0 0 11 8" width="28" height="20">
						<path d="M2,0 h1 v1 h-1z M8,0 h1 v1 h-1z M1,1 h1 v1 h-1z M3,1 h5 v1 h-5z M9,1 h1 v1 h-1z M0,2 h1 v1 h-1z M2,2 h1 v1 h-1z M3,2 h5 v1 h-5z M8,2 h1 v1 h-1z M10,2 h1 v1 h-1z M0,3 h1 v1 h-1z M2,3 h7 v1 h-7z M10,3 h1 v1 h-1z M0,4 h11 v1 h-11z M1,5 h1 v1 h-1z M3,5 h1 v1 h-1z M7,5 h1 v1 h-1z M9,5 h1 v1 h-1z M0,6 h1 v1 h-1z M2,6 h1 v1 h-1z M8,6 h1 v1 h-1z M10,6 h1 v1 h-1z M2,7 h1 v1 h-1z M4,7 h1 v1 h-1z M6,7 h1 v1 h-1z M8,7 h1 v1 h-1z" fill="currentColor"/>
					</svg>
					<h2>My Hobbies</h2>
				</div>
				<p>
					Besides programming, I enjoy bouldering in my free time. I find the physical activity
					challenging, and the routes themselves present interesting puzzles!
				</p>
				<p>
					I also really like animals, both domestic and wild, as well as extinct ones! I have a dog
					named Eddie, and he's the cutest, biggest thing!
				</p>
			</section>
		</div>
	</div>

	<!-- Invader row divider above footer -->
	<div class="invader-row" aria-hidden="true">
		{#each Array(11) as _, i}
			<svg class="row-invader" viewBox="0 0 11 8" width="22" height="16" style="animation-delay: {i * 0.15}s">
				<path d="M2,0 h1 v1 h-1z M8,0 h1 v1 h-1z M1,1 h1 v1 h-1z M3,1 h5 v1 h-5z M9,1 h1 v1 h-1z M0,2 h1 v1 h-1z M2,2 h1 v1 h-1z M3,2 h5 v1 h-5z M8,2 h1 v1 h-1z M10,2 h1 v1 h-1z M0,3 h1 v1 h-1z M2,3 h7 v1 h-7z M10,3 h1 v1 h-1z M0,4 h11 v1 h-11z M1,5 h1 v1 h-1z M3,5 h1 v1 h-1z M7,5 h1 v1 h-1z M9,5 h1 v1 h-1z M0,6 h1 v1 h-1z M2,6 h1 v1 h-1z M8,6 h1 v1 h-1z M10,6 h1 v1 h-1z M2,7 h1 v1 h-1z M4,7 h1 v1 h-1z M6,7 h1 v1 h-1z M8,7 h1 v1 h-1z" fill="currentColor"/>
			</svg>
		{/each}
	</div>

	<!-- Footer -->
	<footer class="footer">
		<div class="footer-content">
			<div class="footer-link">
				<img class="footer-image" src={githubLogo} alt="GitHub logo" />
				<a href="https://github.com/hugobarroca">@hugobarroca</a>
			</div>
			<div class="footer-link">
				<img class="footer-image" src={xLogo} alt="X logo" />
				<a href="https://x.com/TheCodeRex">@TheCodeRex</a>
			</div>
		</div>
	</footer>
	{/if}
</main>

<style lang="scss">
	/* ===== Keyframes ===== */

	@keyframes wave {
		0% {
			d: path('M0,0 C150,120 350,-30 500,20 L500,00 L0,0 Z');
		}
		50% {
			d: path('M0,0 C150,100 350,-50 500,30 L500,00 L0,0 Z');
		}
		100% {
			d: path('M0,0 C150,120 350,-30 500,20 L500,00 L0,0 Z');
		}
	}

	@keyframes reveal {
		0% {
			opacity: 0;
			transform: translateY(20px);
		}
		100% {
			opacity: 1;
			transform: translateY(0);
		}
	}

	@keyframes cursor-blink {
		0%,
		100% {
			opacity: 0;
		}
		50% {
			opacity: 1;
		}
	}

	@keyframes float {
		0%,
		100% {
			transform: translateY(0) translateX(0);
		}
		25% {
			transform: translateY(-15px) translateX(5px);
		}
		50% {
			transform: translateY(-5px) translateX(-5px);
		}
		75% {
			transform: translateY(-20px) translateX(3px);
		}
	}

	@keyframes sway {
		0%,
		100% {
			transform: translateX(0);
		}
		50% {
			transform: translateX(20px);
		}
	}

	@keyframes flicker {
		0%,
		100% {
			opacity: 0.08;
		}
		50% {
			opacity: 0.15;
		}
	}

	@keyframes pulse-glow {
		0%,
		100% {
			box-shadow: 0 0 5px rgba(0, 255, 65, 0.1), inset 0 0 5px rgba(0, 255, 65, 0.05);
		}
		50% {
			box-shadow: 0 0 15px rgba(0, 255, 65, 0.2), inset 0 0 10px rgba(0, 255, 65, 0.08);
		}
	}

	/* ===== Background Invaders ===== */

	.invader-bg {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		pointer-events: none;
		z-index: 0;
		overflow: hidden;
	}

	.invader {
		position: absolute;
		color: rgba(0, 255, 65, 0.07);
		filter: blur(0.5px);
	}

	.invader-1 {
		top: 8%;
		left: 5%;
		animation: float 8s ease-in-out infinite, flicker 4s ease-in-out infinite;
	}
	.invader-2 {
		top: 15%;
		right: 8%;
		animation: float 10s ease-in-out infinite 1s, flicker 5s ease-in-out infinite 0.5s;
	}
	.invader-3 {
		top: 40%;
		left: 3%;
		animation: float 9s ease-in-out infinite 2s, flicker 6s ease-in-out infinite 1s;
	}
	.invader-4 {
		top: 55%;
		right: 4%;
		animation: float 7s ease-in-out infinite 0.5s, flicker 4.5s ease-in-out infinite 1.5s;
	}
	.invader-5 {
		top: 75%;
		left: 8%;
		animation: float 11s ease-in-out infinite 3s, flicker 5.5s ease-in-out infinite 2s;
	}
	.invader-6 {
		top: 85%;
		right: 10%;
		animation: float 8.5s ease-in-out infinite 1.5s, flicker 4s ease-in-out infinite 0.8s;
	}

	/* ===== SVG Wave ===== */

	path {
		fill: var(--primary-bg-color);
		stroke: none;
	}

	svg {
		display: inline-block;
		left: 0;
		position: absolute;
		top: 0;
	}

	.wave {
		animation: wave 5s infinite ease-in-out;
	}

	.container {
		display: inline-block;
		overflow: hidden;
		padding-bottom: 10%;
		position: relative;
		vertical-align: middle;
		width: 100%;
	}

	/* ===== Typography ===== */

	h2 {
		font-family: var(--font-family-display);
		font-size: var(--font-size-h2);
		color: var(--primary-text-color);
		text-shadow: 0 0 10px var(--glow-color), 0 0 20px var(--glow-color);
		margin-bottom: 0.5em;
	}

	h3 {
		font-family: var(--font-family);
		font-size: var(--font-size-h3);
		white-space: nowrap;
		min-width: 1ch;
	}

	/* ===== Terminal Header ===== */

	.terminal-bar {
		display: flex;
		align-items: center;
		gap: 12px;
		padding: 8px 16px;
		background: rgba(0, 255, 65, 0.05);
		border-bottom: 1px solid var(--card-border);
	}

	.terminal-dots {
		display: flex;
		gap: 6px;
	}

	.dot {
		width: 10px;
		height: 10px;
		border-radius: 50%;
	}

	.dot-red {
		background: #ff5f57;
	}
	.dot-yellow {
		background: #ffbd2e;
	}
	.dot-green {
		background: #28c840;
	}

	.terminal-title {
		font-family: var(--font-family);
		font-size: 13px;
		color: var(--secondary-text-color);
		opacity: 0.6;
	}

	.header {
		background-color: var(--primary-bg-color);
		border-bottom: 1px solid var(--card-border);
		position: relative;
		z-index: 1;
	}

	.intro-text {
		padding: 2% 5%;
		text-align: center;
		min-height: 60px;
	}

	.secondary-header {
		color: var(--primary-text-color);
	}

	.fake-code-container {
		align-items: center;
		display: flex;
		height: 100%;
		justify-content: center;
	}

	.prompt-symbol {
		font-family: var(--font-family);
		font-size: var(--font-size-h3);
		color: var(--primary-text-color);
		text-shadow: 0 0 10px var(--glow-color);
	}

	.cursor {
		border-radius: 10px;
		padding: 0;
	}

	.cursor h3::after {
		animation: cursor-blink var(--cursor-blink-duration) steps(1) infinite;
		background: var(--primary-text-color);
		box-shadow: 0 0 6px var(--glow-color);
		content: '';
		display: inline-block;
		height: 1.3em;
		margin-left: 0.1em;
		vertical-align: text-bottom;
		width: 0.1em;
	}

	.flex-center {
		align-items: center;
		display: flex;
		flex-direction: column;
		justify-content: center;
	}

	/* ===== Main Content ===== */

	.general-container {
		align-items: center;
		animation: reveal 0.6s ease-out both;
		display: flex;
		flex-direction: column;
		justify-content: center;
		padding: 2% 5% 5% 5%;
		position: relative;
		z-index: 1;
	}

	.main-content {
		max-width: 900px;
		width: 100%;
		display: flex;
		flex-direction: column;
		gap: 1.5rem;
	}

	/* ===== Section Cards ===== */

	.section-card {
		background: var(--card-bg);
		border: 1px solid var(--card-border);
		border-radius: 4px;
		padding: 1.5rem 2rem;
		position: relative;
		transition: border-color 0.3s ease, box-shadow 0.3s ease;
		animation: pulse-glow 6s ease-in-out infinite;

		&:hover {
			border-color: rgba(0, 255, 65, 0.35);
			box-shadow: 0 0 20px rgba(0, 255, 65, 0.15), inset 0 0 15px rgba(0, 255, 65, 0.05);
		}

		p {
			margin: 0.5rem 0;
		}
	}

	.section-header {
		display: flex;
		align-items: center;
		gap: 0.75rem;
		margin-bottom: 0.5rem;

		h2 {
			margin: 0;
		}
	}

	.section-invader {
		color: var(--primary-text-color);
		filter: drop-shadow(0 0 4px var(--glow-color));
		flex-shrink: 0;
		position: relative;
	}

	/* ===== About / Photo ===== */

	.intro-and-photo {
		display: flex;
		align-items: center;
		gap: 2rem;
		flex-direction: column-reverse;
	}

	.about-text {
		flex: 1;
	}

	.profile-picture-wrapper {
		display: flex;
		justify-content: center;
		width: 40%;
		min-width: 120px;
		max-width: 200px;
		padding: 0.5rem;
	}

	.profile-picture {
		border: 2px solid var(--primary-text-color);
		border-radius: 4px;
		box-shadow: 0 0 15px var(--glow-color), 0 0 30px rgba(0, 255, 65, 0.15);
		height: auto;
		width: 100%;
		filter: grayscale(40%) contrast(1.1) brightness(0.9);
		transition: filter 0.4s ease, box-shadow 0.4s ease;

		&:hover {
			filter: grayscale(0%) contrast(1) brightness(1);
			box-shadow: 0 0 25px var(--glow-color-strong), 0 0 50px var(--glow-color);
		}
	}

	/* ===== Invader Row Divider ===== */

	.invader-row {
		display: flex;
		justify-content: center;
		gap: 1.5rem;
		padding: 2rem 1rem;
		flex-wrap: wrap;
		position: relative;
		z-index: 1;
	}

	.row-invader {
		color: var(--primary-text-color);
		opacity: 0.3;
		animation: sway 3s ease-in-out infinite;
		filter: drop-shadow(0 0 3px var(--glow-color));
		transition: opacity 0.3s ease;

		&:hover {
			opacity: 0.8;
		}
	}

	/* ===== Footer ===== */

	.footer {
		background-color: var(--primary-bg-color);
		border-top: 1px solid var(--card-border);
		padding: 1.5rem 1rem;
		position: relative;
		z-index: 1;
	}

	.footer-content {
		display: flex;
		justify-content: center;
		gap: 3rem;
		flex-wrap: wrap;
	}

	.footer-link {
		display: flex;
		align-items: center;
		gap: 10px;
		transition: transform 0.2s ease;

		&:hover {
			transform: translateY(-2px);
		}

		a {
			color: var(--links-color);
			font-family: var(--font-family);
			font-size: 16px;
			text-decoration: none;

			&:hover {
				color: var(--links-hover-color);
				text-shadow: 0 0 8px var(--glow-color);
			}
		}
	}

	.footer-image {
		height: 24px;
		width: auto;
		filter: brightness(0) invert(1) sepia(1) saturate(5) hue-rotate(85deg) brightness(1.2);
		opacity: 0.8;
		transition: opacity 0.3s ease;
	}

	.footer-link:hover .footer-image {
		opacity: 1;
	}

	/* ===== Responsive ===== */

	@media screen and (min-width: 850px) {
		h2,
		h3 {
			font-size: 42px;
		}

		.intro-and-photo {
			flex-direction: row;
		}

		.profile-picture-wrapper {
			width: 30%;
		}

		.section-card {
			padding: 2rem 2.5rem;
		}

		.general-container {
			padding: 2% 10% 5% 10%;
		}
	}
</style>
