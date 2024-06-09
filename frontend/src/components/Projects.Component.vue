
<template>
    <section id="hero" class="bg-[url('/images/projects-hero.png')] bg-no-repeat backy w-full">
		<div
			class=" h-dvh gap-0 w-full justify-center items-center  border-green-600 border mb-0"
		>
			<div
				class="flex-1 flex-col h-full flex justify-center items-end bg-transparent px-10 md:px-40 mb-0  border-red-600 border mt-16"
			>
				<div class="pb-8 w-full">
					<div
						class="text-8xl font-extrabold flex items-start flex-col gap-5  text-center"
					>
						<span class="w-full drop-shadow-lg">We invest in people who are</span>
						<span class="w-full drop-shadow-lg text-7xl"> Always Passionate</span>
						<span class="w-full drop-shadow-lg text-5xl ">about what they do</span>
					</div>
				</div>
				<div class=" w-full  flex flex-col justify-center text-center gap-10">
					<h3 class="top-startups text-4xl drop-shadow-xl pb-8">See our top Startups</h3>
					<img class="mx-auto h-2/4 pb-10 " src="/images/strarrow.png">
				</div>
				<div class="w-full flex flex-col ">
			<div class="w-full flex justify-center align-center gap-28 text-2xl font-extrabold drop-shadow-2xl pb-16"><a>All</a><a>Trending Startups</a><a>Top Startups</a><a>Latest Startups</a></div>
			</div>
			
			</div>
			<div class="projects-section border-black border justify-items-center bg-[url('/images/projectsglow.png')] bg-no-repeat backy2">
  <div class="project-card">
    <div class="project-thumbnail">
      <img src="/images/hd.jpg" alt="Project 1 thumbnail">
    </div>
    <h2>Project Title 1</h2>
    <p class="subheading">Project Subheading 1</p>
    <p>Project details go here. Lorem ipsum dolor sit amet...</p>
    <button class="details-btn">View Details</button>
  </div>
  <div class="project-card">
    <div class="project-thumbnail">
      <img src="/images/hd.jpg" alt="Project 2 thumbnail">
    </div>
    <h2>Project Title 2</h2>
    <p class="subheading">Project Subheading 2</p>
    <p>Project details go here. Lorem ipsum dolor sit amet...</p>
    <button class="details-btn">View Details</button>
  </div>
  <div class="project-card">
    <div class="project-thumbnail">
      <img src="/images/hd.jpg" alt="Project 3 thumbnail">
    </div>
    <h2>Project Title 3</h2>
    <p class="subheading">Project Subheading 3</p>
    <p>Project details go here. Lorem ipsum dolor sit amet...</p>
    <button class="details-btn">View Details</button>
  </div>
  <div class="project-card">
    <div class="project-thumbnail">
      <img src="/images/hd.jpg" alt="Project 4 thumbnail">
    </div>
    <h2>Project Title 4</h2>
    <p class="subheading">Project Subheading 4</p>
    <p>Project details go here. Lorem ipsum dolor sit amet...</p>
    <button class="details-btn">View Details</button>
  </div>
</div>
		
		</div>
		
	</section>
</template>
<style scoped>
.backy{
	background-size: cover;
	background-position: 75% 0%;
}
.backy2{
	background-size: cover;
	background-position: 100% 0%;
}
.top-startups{
	color:rgb(254, 145, 104);
}
.drop-shadow-xl {
    filter: drop-shadow(0 5px 10px rgba(254, 145, 104,0.40)); /* Red color with opacity */
  }

.projects-section {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* Defines two columns of equal width */
  grid-gap: 20px; /* Optional spacing between project cards */
  
}

.project-card {
  width: 625px;
  height: 575px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 20px; /* Adds padding for content */
}

.project-card h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

.project-card .subheading,
.project-card .details-btn {
  margin-top: 10px;
}

.project-card .subheading {
  font-size: 16px;
  color: #666;
}

.project-card .details-btn {
  background-color: #007bff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.project-thumbnail {
  width: 100%; /* Stretches to full card width */
  height: 200px; /* Adjust height as needed */
  margin-bottom: 10px; /* Adds spacing below the image */
  overflow: hidden; /* Ensures image doesn't overflow container */
}

.project-thumbnail img {
  width: 100%; /* Stretches image to fit container */
  height: 100%; /* Stretches image to fit container */
  object-fit: cover; /* Scales image to cover the container */
}
</style>