<main>
	<div id="main-content">
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
			<!-- xmlns="http://www.w3.org/2000/svg"
            style="transform:translate(0, 0px); opacity:1"
            fill="url(#sw-gradient-0)" -->
			<path d="M0,0 C150,120 350,-30 500,20 L500,00 L0,0 Z"></path>
		</svg>
	</div>
</main>

<style>
	#main-content {
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
		animation: cursor-blink 1.5s steps(2) infinite;
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
		font-size: 5em;
		justify-content: center;
	}

	h2 {
		display: flex;
		font-size: 3em;
		justify-content: center;
	}

	h3 {
		display: flex;
		font-size: 3em;
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
