<script setup lang="ts">
import { ref, computed } from "vue"
import { DateFormatter, type DateValue, getLocalTimeZone } from "@internationalized/date"

import { Calendar as CalendarIcon } from "lucide-vue-next"
import { Calendar } from "@/shared/shadcn-ui/ui/calendar"
import { Button } from "@/shared/shadcn-ui/ui/button"
import { Popover, PopoverContent, PopoverTrigger } from "@/shared/shadcn-ui/ui/popover"
import { cn } from "@/libs/utils"

const props = defineProps<{ class: string; defaultValue?: DateValue | Date }>()
const df = new DateFormatter("en-US", {
	dateStyle: "long"
})

let currentValue: DateValue = props?.defaultValue as DateValue
const value = ref<DateValue>()
const emit = defineEmits<{
	(e: "ondatechanged", date: any): void
}>()

computed(() => {
	console.log(value.value)
	if (currentValue !== value.value) {
		currentValue = value.value as DateValue
		console.log(value.value, "onDateChanged Triggered")
		emit("ondatechanged", currentValue)
	}
	return value.value
})
</script>

<template>
	<Popover>
		<PopoverTrigger as-child>
			<Button
				variant="outline"
				:class="
					cn(
						'w-[280px] justify-start text-left font-normal',
						!value && 'text-muted-foreground',
						props.class
					)
				"
			>
				<CalendarIcon class="mr-2 h-4 w-4" />
				{{ value ? df.format(value.toDate(getLocalTimeZone())) : "Pick a date" }}
			</Button>
		</PopoverTrigger>
		<PopoverContent class="w-auto p-0">
			<Calendar v-model="value" initial-focus />
		</PopoverContent>
	</Popover>
</template>
