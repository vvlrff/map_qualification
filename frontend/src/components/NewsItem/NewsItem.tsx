import dayjs from "dayjs"
import { Link } from "react-router-dom"
import s from "./NewsItem.module.scss"
import { INews } from "../../models/INews"


const NewsItem = (news: INews) => {
    return (
        <div>
            <Link to={`/data/${news.id}`} className={s.link}>
                <div key={news.id} className={s.item}>
                    <img src={news.image} alt="img" />
                    <div className={s.title}>{news.title_ru}</div>
                    <div>Дата: {dayjs(news.date).format('DD-MM-YYYY')}</div>
                </div>
            </Link>
        </div>
    )
}

export default NewsItem