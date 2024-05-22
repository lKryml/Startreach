<template>
	<!-- bg-[url('https://cdn.dribbble.com/userupload/12700543/file/original-2f761db0abe85c110884800f36395c9e.png?resize=1600x1200')] -->
	<section id="hero">
		<div
			class="grid pt-[70px] grid-col-1 md:grid-cols-2 h-dvh gap-0 w-full justify-center items-center"
		>
			<div
				class="flex-1 hidden h-full md:flex justify-center items-end bg-transparent p-4 md:p-10"
			>
				<div
					class="w-full h-full rounded-xl bg-[url('https://cdn.dribbble.com/userupload/12700543/file/original-2f761db0abe85c110884800f36395c9e.png?resize=1600x1200')]"
				></div>
			</div>
			<div
				class="flex-1 flex-col h-full flex justify-center items-end bg-transparent px-10 md:px-40"
			>
				<div class="pb-7 w-full">
					<div
						class="text-6xl font-extrabold flex justify-end items-start flex-col gap-5 grid-flow-col"
					>
						<span class="w-full text-end">Empowering</span>
						<span class="w-full text-end">Entreprenuers</span>
						<span class="w-full text-end">to Connect Investors</span>
					</div>
				</div>
				<div class="flex justify-center items-start pb-7 md:1/2 w-full">
					<div class="self-end text-end">
						Empowering Entreprenuers to Connect Investors, Empowering Entreprenuers to
						Connect InvestorsEmpowering Entreprenuers to Connect Investors
					</div>
				</div>

				<div
					class="text-foreground flex flex-row-reverse justify-end items-center text-lg md:text-md font-bold"
				>
					<Button
						class="cursor-pointer rounded-full shadow-none ms-4 w-60 md:w-45 sm:w-30 h-14 bg-secondary text-secondary-foreground"
						><router-link to="/auth/register">{{
							t("GENERAL.GET_STARTED")
						}}</router-link></Button
					>
					<Button
						class="cursor-pointer rounded-full shadow-none w-60 md:w-45 sm:w-30 h-14 bg-transparent border-primary border-[2px] text-foreground"
						>{{ t("GENERAL.CONTACT_US") }}</Button
					>
				</div>
			</div>
		</div>
	</section>
	<section id="partners">
		<div class="w-full flex flex-row gap-20 justify-around items-center h-[120px] bg-accent">
			<div
				v-for="(_, index) in partnersImagesPaths"
				:key="index"
				class="w-24 max-h-20 justify-center items-center"
			>
				<img :src="_" />
			</div>
		</div>
	</section>
</template>

<script setup lang="ts">
import { Carousel, CarouselPrevious, CarouselNext } from "@/shared/shadcn-ui/ui/carousel"
import { partnersImagesPaths } from "@/constants/partners.contant"
import { useI18n } from "vue-i18n"
const { t } = useI18n()
</script>
