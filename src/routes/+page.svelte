<main>
	<div id="header">
		<div id="intro-text">
			<h2>Hey!</h2>
			<h1>I'm Hugo Barroca</h1>
			<div id="fake-code-container">
				<span class="cursor">
					<h3>&lt;Software Developer /&gt;</h3>
				</span>
			</div>
		</div>
		<div id="pf-section">
			<img id="profile-picture" height="600vh" src="public/static/Me.jpeg" alt="Me" />
		</div>
	</div>
	<div class="container">
		<svg viewBox="0 0 500 500" preserveAspectRatio="xMinYMin meet">
			<path d="M0,0 C150,120 350,-30 500,20 L500,00 L0,0 Z"></path>
		</svg>
	</div>
	<div id="main-content">
		<h2>About me</h2>
		<p>
			I'm a software developer with a passion for technology and innovation. I'm always looking for new challenges and opportunities to learn and grow.
		</p>
		<h2>Skills</h2>
		<ul>
			<li>.NET</li>
			<li>C#</li>
			<li>JavaScript</li>
			<li>React</li>

		</ul>
	</div>
</main>

<style>
	#header {
		background-color: #333;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: space-around;
		padding-top: 50px;
	}

	#fake-code-container {
		display: flex;
		align-items: center;
		justify-content: center;
		height: 100%;
	}

	#profile-picture {
		border-radius: 50%;
		height: auto;
		width:100%
	}

	.cursor {
		padding: 0 50px 0 10px;
		border-radius: 10px;
	}

	@keyframes cursor-blink {
		0% {
			opacity: 0;
		}
	}

	.cursor h3::after {
		content: '';
		width: 5px;
		height: 45px;
		background: #f7f7f7;
		display: inline-block;
		animation: cursor-blink 2.5s steps(2) infinite;
	}

	.cursor h3 {
		display: flex;
		align-items: center;
		gap: 2px;
	}

	path {
		stroke: none;
		fill: #333;
	}

	h1 {
		display: flex;
		font-size: 5vw;
		justify-content: center;
	}

	h2 {
		display: flex;
		font-size: 4vw;
		justify-content: center;
	}

	h3 {
		text-wrap: nowrap;
		display: flex;
		font-size: 3vw;
		justify-content: center;
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
		padding-bottom: 100%;
		vertical-align: middle;
		overflow: hidden;
	}
</style>
