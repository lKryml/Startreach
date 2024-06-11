
<template>	
	<!-- bg-[url('https://cdn.dribbble.com/userupload/12700543/file/original-2f761db0abe85c110884800f36395c9e.png?resize=1600x1200')] -->
	<section id="hero" class="bg-[url('https://cdn.builder.io/api/v1/image/assets%2F972274c44a2d4c658b0fa440848d24a1%2Fc0c09fcb7f514c239a5ae143472a3770?format=webp&width=2000')] backy bg-no-repeat">
		<div
			class="grid pt-[70px] grid-col-1 md:grid-cols-2 h-dvh gap-0 w-full justify-center items-center"
		>
			<div
				class="flex-1 flex-col h-full flex justify-center items-end bg-transparent px-10 md:px-40"
			>
				<div class="pb-7 w-full">
					<div
						class="text-6xl font-extrabold flex items-start flex-col gap-5 grid-flow-col"
					>
						<span class="w-full ">Empowering Entreprenuers to Connect Investors</span>
						
					</div>
				</div>
				<div class="flex justify-center items-start pb-7 md:1/2 w-full">
					<div class="self-end ">
						Empowering Entreprenuers to Connect Investors, Empowering Entreprenuers to
						Connect InvestorsEmpowering Entreprenuers to Connect Investors
					</div>
				</div>

				<div
					class="text-foreground flex flex-row-reverse justify-start items-center text-lg md:text-md font-bold mr-auto   "
				>
					<router-link to="/auth/register">
						<Button
							class="cursor-pointer rounded-full shadow-none ms-4 w-60 md:w-45 sm:w-30 h-14 bg-secondary text-secondary-foreground "
							>{{ t("GENERAL.GET_STARTED") }}</Button
						>
					</router-link>

					<router-link to="/about">
						<Button
							class="cursor-pointer rounded-full shadow-none w-60 md:w-45 sm:w-30 h-14 bg-transparent border-primary border-[2px] text-foreground"
							>{{ t("GENERAL.CONTACT_US") }}</Button
						></router-link>
				</div>
			</div>
			<!-- <div
				class="flex-1 hidden h-full md:flex justify-center items-end bg-transparent p-4 md:p-10"
			>
				<div
					class="w-full h-full rounded-xl bg-[url('https://cdn.dribbble.com/userupload/12700543/file/original-2f761db0abe85c110884800f36395c9e.png?resize=1600x1200')]"
				></div>
			</div> -->
		</div>
	</section>
	
</template>
<style scoped>
.backy{
	background-size:cover;
}
text{
    color: #fe9168;
}
</style>





<!-- <template>
    <div class=" container w-full h-full flex flex-col bg-[url('https://cdn.builder.io/api/v1/image/assets%2F972274c44a2d4c658b0fa440848d24a1%2Fc0c09fcb7f514c239a5ae143472a3770?format=webp&width=2000')] bg-no-repeat bg-cover">
        <div class="w-full h-full"><p>hello</p></div>
    </div>
</template> -->