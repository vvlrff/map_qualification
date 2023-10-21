export interface INews {
    id: number,
    title_en: string,
    title_ru: string,
    date: string,
    href: string,
    image: string,
    image_text_en: string,
    image_text_ru: string,
    country: string[],
    city: string[] 
};