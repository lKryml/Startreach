import { enviroment } from "@/enviroments/enviroment"
import type { Ref } from "vue"

interface AssignFileProps {
    translator: any,
    signal: Ref<string>,
    $event: any,
    fileType?: 'image' | 'document',
    toast: any
}

export const assignFileFromInput = async (options: AssignFileProps) => {
    const { $event, translator, signal, toast, fileType } = options;
    const file: File = $event.target.files[0]

    signal.value = ""
    if ((fileType === 'image' && !enviroment.allowed_images_types.includes(file.type))
        || (fileType === 'document' && !enviroment.allowed_files_types.includes(file.type))) {
        toast({
            variant: "destructive",
            title: translator("GENERAL.ERROR"),
            description: `${translator("GENERAL.FILE_TYPE_NOT_ALLOWED_TO_BE_UPLOAD")} (${enviroment.max_image_size_by_mb})`
        })
    }
    if (file.size / (1024 * 1024) > (fileType === 'image' ? enviroment.max_image_size_by_mb : enviroment.max_file_size_by_mb)) {
        toast({
            variant: "destructive",
            title: translator("GENERAL.ERROR"),
            description: `${translator("GENERAL.IMAGE_SIZE_EXCEEDED")} (${enviroment.max_image_size_by_mb})`
        })
    }
    signal.value = await file.text()
}