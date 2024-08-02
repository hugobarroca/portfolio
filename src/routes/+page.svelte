<script lang="ts">
	import '../app.css';
	import { onMount } from 'svelte';
	import githubLogo from '/static/icons/github-mark.svg';
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
			<div id="fake-code-container">
				<span class="cursor">
					<h3>I am a &lt;Software Developer /&gt;</h3>
				</span>
			</div>
		</div>
	</div>
	<div class="container">
		<svg viewBox="0 0 500 500" preserveAspectRatio="xMinYMin meet">
			<path id="wave" d="M0,0 C150,120 350,-30 500,20 L500,00 L0,0 Z"></path>
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
				I'm a software developer with a passion for technology and innovation 🚀. I'm always looking
				for new challenges and opportunities to learn and grow! 🌱
			</p>

			<p>
				I'm currently working as a backend developer at Create IT, providing services for a major
				Portuguese e-commerce company. 🚚
			</p>

			<p>
				I've worked with a variety of technologies, but the bulk of my experience has been with C#
				and Microsoft technologies, from .NET Core 3.5 to .NET 8. I've developed multiple web
				applications, APIs, and services, and have been working with Azure services for the past
				year.
			</p>

			<p>I'm am currently studying for my second Azure certification, (DevOps Expert). 📖</p>

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
		<div class="github-link">
			<img src={githubLogo} alt="github logo" />
			<a href="https://github.com/hugobarroca"><p>@hugobarroca</p></a>
		</div>
	</footer>
</main>

<style>
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

	.intro-and-photo {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
	}

	.profile-picture-wrapper {
		display: flex;
		align-items: right;
		justify-content: right;
		width: 50%;
	}
	.profile-picture {
		border-style: solid;
		border-color: darkkhaki;
		border-radius: 50%;
		width: 100%;
		height: auto;
	}

	#wave {
		animation: wave 5s infinite ease-in-out;
	}

	.starter-content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 1vh;
	}

	.greeting {
		animation: revealanddisappear 2.8s cubic-bezier(0.215, 0.61, 0.355, 1) 0.25s backwards;
		font-size: 20vmin;
		opacity: 0%;
	}

	.my-name-is {
		margin: 10%;
		animation: revealanddisappear 2.8s cubic-bezier(0.215, 0.61, 0.355, 1) 2.25s backwards;
		opacity: 0%;
		font-size: 10vmin;
	}

	#fake-code-container {
		display: flex;
		align-items: center;
		justify-content: center;
		height: 100%;
		animation: reveal 1.3s cubic-bezier(0.215, 0.61, 0.355, 1) 5.25s backwards;
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
		text-align: center;
		padding: 5%;
		max-height: 10%;
	}

	.cursor {
		padding: 0;
		border-radius: 10px;
	}

	.cursor h3::after {
		content: '';
		width: 0.1em;
		height: 1.3em;
		margin-left: 0.1em;
		background: var(--text-color);
		display: inline-block;
		animation: cursor-blink var(--cursor-blink-duration) steps(1) infinite;
		vertical-align: text-bottom;
	}

	.flex-center {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	path {
		stroke: none;
		fill: var(--primary-bg-color);
	}

	h2 {
		font-family: var(--font-family);
		font-size: var(--font-size-h2);
	}

	h3 {
		white-space: nowrap;
		font-family: var(--font-family);
		font-size: var(--font-size-h3);
	}

	svg {
		display: inline-block;
		position: absolute;
		top: 0;
		left: 0;
	}

	.container {
		display: inline-block;
		position: relative;
		width: 100%;
		padding-bottom: 10%;
		vertical-align: middle;
		overflow: hidden;
	}

	.general-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 10%;
		padding-top: 0%;
		font-size: var(--font-size-h2);
		animation: reveal 1.3s cubic-bezier(0.215, 0.61, 0.355, 1) 5.25s backwards;
	}

	.main-content {
		max-width: 1050px;
	}

	.footer {
		color: whitesmoke;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
		background-color: var(--primary-bg-color);
		padding: 1vh;
	}

	.github-link {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
		/* <!-- Strip style from links--> */
		text-decoration: none;
		color: whitesmoke;
	}

	.github-link a {
		color: #a5a5a5;
	}

	.github-link img {
		width: 50px;
		height: auto;
		padding-right: 15px;
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
