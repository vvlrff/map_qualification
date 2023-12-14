export interface INews {
    id: number,
    title_en: string,
    title_ru: string,
    date: string,
    href: string,
    image: string,
    country: string[],
    city: string[],
    topical_keywords: string[]
};