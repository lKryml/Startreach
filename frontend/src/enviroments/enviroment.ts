const PORT = 8000;

export const enviroment = {
    enviroment: 'development',
    baseUrl: `http://localhost:${PORT}`,
    apiUrl: `http://localhost:${PORT}/api`,
    apiPort: `${PORT}`,

    allowed_files_types: ['application/pdf'],
    allowed_images_types: ['image/png', 'image/jpeg', 'image/jpg', 'image/gif'],
    max_image_size_by_mb: 5,
    max_file_size_by_mb: 10,
}