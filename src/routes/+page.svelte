<script lang="ts">
	import '../app.css';
	import { onMount } from 'svelte';
	import githubLogo from '/static/icons/github-mark.svg';
	import xLogo from '/static/icons/x-logo.svg';
	import profilePhoto from '/static/Me.jpeg';

	let starterContent: HTMLElement;
	let starterContentRemovalTimer: number = 4500;

	onMount(() => {
		let greeting = Array.from(starterContent.children)[0];
		let myName = Array.from(starterContent.children)[1];

		setTimeout(() => greeting.remove(), 2200);
		setTimeout(() => myName.remove(), starterContentRemovalTimer);
		setTimeout(() => starterContent.remove(), starterContentRemovalTimer);
	});
</script>

<main>
	<div class="header">
		<div class="intro-text flex-center">
			<div class="fake-code-container">
				<span class="cursor">
					<h3 class="secondary-header">I am a &lt;Software Developer /&gt;</h3>
				</span>
			</div>
		</div>
	</div>
	<div class="container">
		<svg viewBox="0 0 500 500" preserveAspectRatio="xMinYMin meet">
			<path class="wave" d="M0,0 C150,120 350,-30 500,20 L500,00 L0,0 Z"></path>
		</svg>
	</div>
	<div bind:this={starterContent} class="starter-content">
		<h2 class="greeting">Hey!</h2>
		<h2 class="my-name-is">My name is Hugo Barroca</h2>
	</div>

	<div class="general-container">
		<div class="main-content">
			<div class="intro-and-photo">
				<h2>About me 👋</h2>

				<div class="profile-picture-wrapper">
					<img class="profile-picture" src={profilePhoto} alt="Hugo Barroca" />
				</div>
			</div>
			<p>
				I'm a software developer with a passion for technology and innovation 🚀 I'm always looking
				for new challenges and opportunities to learn and grow! 🌱
			</p>

			<h2>My Current Job 🏢</h2>

			<p>
				I've been working as a backend developer at Create IT since 2021, providing my services as a
				fullstack software developer for a major Portuguese e-commerce company. 🚚
			</p>

			<h2>Teck Stack ⚙️</h2>

			<p>
				I've developed multiple web applications, APIs, and services, both on-prem and utilizing
				Azure services. ☁️
			</p>

			<p>
				I've worked with a variety of technologies, but the bulk of my experience has been with C#
				and .NET, as well as FE frameworks such as React and Svelte. 🛠️
			</p>

			<h2>Certifications 📃</h2>

			<p>
				I'm certified as an Azure Developer (AZ-204), and I'm am currently studying for my second
				Azure certification, (DevOps Expert). 📖
			</p>

			<h2>My Projects 🎯</h2>
			<p>
				I'm currently working on a Chrome extension to help redirect you away from distracting
				sites! It's a work in progress, so I'll update you soon. 🚧
			</p>

			<h2>My Hobbies 🌴</h2>
			<p>
				Besides programming, I enjoy bouldering in my free time 🧗‍♂️. I find the physical activity
				challenging, and the routes themselves present interesting puzzles!
			</p>

			<p>
				I also really like animals, both domestic and wild, as well as extinct ones! 🦖 I have a dog
				🐾 named Eddie, and he's the cutest, biggest thing!
			</p>
		</div>
	</div>
	<footer class="footer">
		<div class="footer-link">
			<img class="footer-image" src={githubLogo} alt="github logo" />
			<a href="https://github.com/hugobarroca"><p>@hugobarroca</p></a>
		</div>
		<div class="footer-link">
			<img src={xLogo} alt="X logo" />
			<a href="https://x.com/TheCodeRex"><p>@TheCodeRex</p></a>
		</div>
	</footer>
</main>

<style lang="scss">
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
			transform: translateY(10vh);
		}
		100% {
			opacity: 1;
			transform: translateY(0);
		}
	}

	@keyframes revealanddisappear {
		0% {
			opacity: 0;
			transform: translateY(10vh);
		}
		50% {
			opacity: 1;
			transform: translateY(0);
		}
		100% {
			opacity: 0;
			transform: translateY(-10vh);
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

	path {
		fill: var(--primary-bg-color);
		stroke: none;
	}

	h2 {
		font-family: var(--font-family);
		font-size: var(--font-size-h2);
	}

	h3 {
		font-family: var(--font-family);
		font-size: var(--font-size-h3);
		white-space: nowrap;
	}

	svg {
		display: inline-block;
		left: 0;
		position: absolute;
		top: 0;
	}

	.secondary-header {
		color: var(--secondary-text-color);
	}

	.intro-and-photo {
		align-items: center;
		display: flex;
		flex-direction: column-reverse;
		justify-content: space-between;
	}

	.profile-picture-wrapper {
		display: flex;
		justify-content: right;
		width: 40%;
		min-width: 150px;
		padding: 2%;
	}
	.profile-picture {
		border-color: var(--highlights-color);
		border-radius: 50%;
		border-style: solid;
		height: auto;
		width: 100%;
	}

	.wave {
		animation: wave 5s infinite ease-in-out;
	}

	.starter-content {
		align-items: center;
		display: flex;
		flex-direction: column;
		justify-content: center;
		padding: 1vh;
	}

	.greeting {
		animation: revealanddisappear 2.8s cubic-bezier(0.215, 0.61, 0.355, 1) 0.25s backwards;
		font-size: 20vmin;
		opacity: 0%;
	}

	.my-name-is {
		animation: revealanddisappear 2.8s cubic-bezier(0.215, 0.61, 0.355, 1) 2.25s backwards;
		font-size: 10vmin;
		margin: 10%;
		opacity: 0%;
	}

	.fake-code-container {
		align-items: center;
		animation: reveal 1.3s cubic-bezier(0.215, 0.61, 0.355, 1) 5.25s backwards;
		display: flex;
		height: 100%;
		justify-content: center;
	}

	.header {
		align-items: center;
		background-color: var(--primary-bg-color);
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		margin-top: -2vh;
		padding-top: 1vh;
	}

	.intro-text {
		max-height: 10%;
		padding: 5%;
		text-align: center;
	}

	.cursor {
		border-radius: 10px;
		padding: 0;
	}

	.cursor h3::after {
		animation: cursor-blink var(--cursor-blink-duration) steps(1) infinite;
		background: var(--text-color);
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

	.container {
		display: inline-block;
		overflow: hidden;
		padding-bottom: 10%;
		position: relative;
		vertical-align: middle;
		width: 100%;
	}

	.general-container {
		align-items: center;
		animation: reveal 1.3s cubic-bezier(0.215, 0.61, 0.355, 1) 5.25s backwards;
		display: flex;
		flex-direction: column;
		font-size: var(--font-size-h2);
		justify-content: center;
		padding: 0% 10% 10% 10%;
	}

	.main-content {
		max-width: 1050px;
		display: flex;
		flex-direction: column;
		h2 {
			align-self: center;
		}
	}

	.footer {
		align-items: center;
		background-color: var(--primary-bg-color);
		color: var(--links-color);
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		padding: 1vh;
	}

	.footer-link {
		align-items: center;
		color: var(--links-color);
		display: flex;
		flex-direction: row;
		height: auto;
		justify-content: center;
		text-decoration: none;
		width: 50%;
	}

	.footer-link a {
		color: var(--links-color);
	}

	.footer-link img {
		height: 30px;
		padding-right: 15px;
		width: auto;
	}

	@media screen and (min-width: 850px) {
		.header {
			max-height: 150px;
		}
		h2,
		h3 {
			font-size: 46px;
		}
	}
</style>
