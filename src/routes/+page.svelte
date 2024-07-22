<main>
	<div id="main-content">
		<div id="intro-text">
			<h2>Hey!</h2>
			<h1>I'm Hugo Barroca</h1>
			<h3>&lt;Software Developer /&gt;</h3>
		</div>
		<div id="pf-section">
			<img id="profile-picture" height="600vh" src="public/static/Me.jpeg" alt="Me" />
		</div>
	</div>
	<div class="container">
		<svg viewBox="0 0 500 500" preserveAspectRatio="xMinYMin meet">
			<path d="M0,70 C150,200 350,0 500,100 L500,00 L0,0 Z" style="stroke: none; fill:#333;"></path>
		</svg>
	</div>
</main>

<style>
	/* Global styles specific to this page */
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

	#main-content {
		background-color: #333;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: space-around;
		padding-top: 50px;
	}

	#profile-picture {
		border-radius: 50%;
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

	#intro-text {
	}
</style>
