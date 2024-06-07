import { ar, en } from "@/constants/i18n"
import { createI18n } from "vue-i18n"

export const i18n = createI18n({
	// something vue-i18n options here ...
	fallbackLocale: "ar",
	locale: "ar",
	silentTranslationWarn: true,
	globalInjection: true,
	legacy: false,
	fallbackWarn: true,
	messages: { ar, en }
})
