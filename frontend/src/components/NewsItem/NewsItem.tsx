import dayjs from "dayjs"
import { Link } from "react-router-dom"
import { INews } from "../../models/INews"
import s from "./NewsItem.module.scss"


const NewsItem = ({ news }: { news: INews }) => {
  return (
    <>
      <Link to={`/data/${news.id}`} className={s.link}>
        <div key={news.id} className={s.item}>
          <div className={s.imgContainer}>
            <img className={s.img} src={news.image} alt="img" />
          </div>
          <div className={s.textContainer}>
            <div className={s.title}>{news.title_ru}</div>
            <div className={s.text}>en: {news.title_en}</div>
            <div className={s.text}>img_text_en: {news.image_text_en}</div>
            <div className={s.text}>img_text_ru: {news.image_text_ru}</div>
            <div>Страны: {news.country.length > 1 ? (
              <span>
                {news.country.map(country => (
                  <span> {country}</span>
                ))}
              </span>
            ) : (
              <span>
                {news.country}
              </span>
            )}</div>
            <div>Города: {news.city}</div>
            <div className={s.date}>Дата: {dayjs(news.date).format('DD-MM-YYYY')}</div>
          </div>
        </div>
      </Link>
    </>
  )
}

export default NewsItem