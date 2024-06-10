<script setup lang="ts">
// import { Carousel, CarouselPrevious, CarouselNext } from "@/shared/shadcn-ui/ui/carousel"
import LearnMoreCardComponent from "@/components/LearnMoreCard.Component.vue"
import { partnersImagesPaths } from "@/constants/partners.contant"
import { useI18n } from "vue-i18n"

import {
	Accordion,
	AccordionContent,
	AccordionItem,
	AccordionTrigger
} from "@/shared/shadcn-ui/ui/accordion"

const accordionItems = [
	{
		value: "1",
		title: "Is it accessible?",
		content: "Yes. It adheres to the WAI-ARIA design pattern."
	},
	{
		value: "2",
		title: "Is it unstyled?",
		content: "Yes. It's unstyled by default, giving you freedom over the look and feel."
	},
	{
		value: "3",
		title: "Can it be animated?",
		content: "Yes! You can use the transition prop to configure the animation."
	}
]

const { t } = useI18n()
const outServicesArray = [
	{
		icon: "FileCog2",
		title: "Title number 1",
		description:
			"fd sfsfd sdfsd s d fsdf sdf sdf sdf sd s dfsd fsd dsf  sdfsdfsdf sdfsd sdf sdfsdf sdf fd sfsfd sdfsd s d fsdf sdf sdf sdf sd s dfsd fsd dsf  sdfsdfsdf sdfsd sdf sdfsdf sdf ",
		path: ""
	},
	{
		icon: "FileCog2",
		title: "Title number 1",
		description:
			"fd sfsfd sdfsd s d fsdf sdf sdf sdf sd s dfsd fsd dsf  sdfsdfsdf sdfsd sdf sdfsdf sdf fd sfsfd sdfsd s d fsdf sdf sdf sdf sd s dfsd fsd dsf  sdfsdfsdf sdfsd sdf sdfsdf sdf ",
		path: ""
	},
	{
		icon: "FileCog2",
		title: "Title number 1",
		description:
			"fd sfsfd sdfsd s d fsdf sdf sdf sdf sd s dfsd fsd dsf  sdfsdfsdf sdfsd sdf sdfsdf sdf fd sfsfd sdfsd s d fsdf sdf sdf sdf sd s dfsd fsd dsf  sdfsdfsdf sdfsd sdf sdfsdf sdf ",
		path: ""
	},
	{
		icon: "FileCog2",
		title: "Title number 1",
		description:
			"fd sfsfd sdfsd s d fsdf sdf sdf sdf sd s dfsd fsd dsf  sdfsdfsdf sdfsd sdf sdfsdf sdf fd sfsfd sdfsd s d fsdf sdf sdf sdf sd s dfsd fsd dsf  sdfsdfsdf sdfsd sdf sdfsdf sdf ",
		path: ""
	},
	{
		icon: "FileCog2",
		title: "Title number 1",
		description:
			"fd sfsfd sdfsd s d fsdf sdf sdf sdf sd s dfsd fsd dsf  sdfsdfsdf sdfsd sdf sdfsdf sdf fd sfsfd sdfsd s d fsdf sdf sdf sdf sd s dfsd fsd dsf  sdfsdfsdf sdfsd sdf sdfsdf sdf ",
		path: ""
	}
]
</script>
<template>	
	<!-- bg-[url('https://cdn.dribbble.com/userupload/12700543/file/original-2f761db0abe85c110884800f36395c9e.png?resize=1600x1200')] -->
	<section id="hero" class="bg-[url('/images/hero-pattern.png')] backy bg-no-repeat">
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
	<section id="partners">
		<div class="w-full flex justify-around items-center h-[120px]">
			<p class="text-5xl font-extrabold">Our Business Partners</p>
		</div>
		<div class="w-full flex flex-row gap-20 justify-around items-center h-[120px] bg-accent">
			<div
				v-for="(_, index) in partnersImagesPaths"
				:key="index" 
				class="w-24 max-h-20 justify-center items-center grayscale"
			>
				<img :src="_" />
			</div>
		</div>
	</section>

	<section id="partners" class="container my-14">
		<div class="w-full flex flex-col justify-around items-start md:pt-20 pt-8">
			<p class="text-lg font-normal text-primary">Out Services</p>
			<p class="text-5xl font-extrabold">Benefits You Get When</p>
			<p class="text-5xl font-extrabold">Using Our Services</p>
		</div>
		<div class="flex flex-row gap-5 flex-wrap justify-center items-center md:p-20 p-8">
			<template v-for="(item, index) of outServicesArray" :key="index">
				<LearnMoreCardComponent
					class="w-full md:w-[350px] md:h-[400px] rounded-md bg-dashboard border-border border-[1px] border-b-[3px] my-10 bg-sky-100"
					:icon="item.icon"
					:title="item.title"
					:description="item.description"
					:path="item.path"
					:leanMoreTitle="t('GENERAL.LEARN_MORE')"
				></LearnMoreCardComponent>
			</template>
		</div>
	</section>

	<section id="questions" class="container">
		<div class="w-full grid gap-4 md:grid-flow-row md:grid-cols-3 grid-flow-col">
			<div class="w-full flex flex-col justify-start items-start">
				<p class="text-5xl font-extrabold mb-4">Frequently</p>
				<p class="text-5xl font-extrabold">Asked Question</p>
			</div>
			<div class="text-lg col-span-2 grid-cols-2">
				<Accordion
					type="single"
					class="w-full"
					collapsible
					:default-value="accordionItems[0].value"
				>
					<AccordionItem
						v-for="item in accordionItems"
						:key="item.value"
						:value="item.value"
					>
						<AccordionTrigger class="text-2xl font-bold">{{
							item.title
						}}</AccordionTrigger>
						<AccordionContent class="text-2xl">
							{{ item.content }}
						</AccordionContent>
					</AccordionItem>
				</Accordion>
			</div>
		</div>
	</section>
</template>
<style scoped>
.backy{
	background-size:cover;
}
</style>