
<template>
    <section id="hero" class="bg-[url('/images/projects-hero.png')] bg-no-repeat backy w-full">
		<div
			class=" h-dvh gap-0 w-full justify-center items-center"
		>
			<div
				class="flex-1 flex-col h-full flex justify-center items-end bg-transparent px-10 md:px-40"
			>
				<div class="pb-7 w-full">
					<div
						class="text-5xl font-extrabold flex items-start flex-col gap-5 "
					>
						<span class="w-full ">We invest in people who are Always Passionate about what they do</span>
						
					</div>
				</div>
				<div class="flex justify-center items-start pb-7 md:1/2 w-full">
					<div class="self-end ">
						Empowering Entreprenuers to Connect Investors, Empowering Entreprenuers to
						Connect InvestorsEmpowering Entreprenuers to Connect Investors
					</div>
				</div>

				<div
					class="text-foreground flex flex-row-reverse justify-start items-center text-lg md:text-md font-bold   "
				>
					<router-link to="/auth/register">
						<Button
							class="cursor-pointer rounded-full shadow-none ms-4 w-60 md:w-45 sm:w-30 h-14 bg-secondary text-secondary-foreground "
							>awdaw</Button
						>
					</router-link>

					<router-link to="/about">
						<Button
							class="cursor-pointer rounded-full shadow-none w-60 md:w-45 sm:w-30 h-14 bg-transparent border-primary border-[2px] text-foreground"
							>dawdawdaw</Button
						></router-link>
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
</style>