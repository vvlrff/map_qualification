import { useParams } from "react-router-dom";
import { newsApi } from "../../services/newsApi";
import s from "./IdPage.module.scss";

const IdPage = () => {
    const { id } = useParams();
    const numberId = Number(id);

    const { data } = newsApi.useGetNewsByIdQuery(numberId);

    return (
        <section className={s.section}>
            <img src={data?.image} className={s.img} alt="articlePhoto" />
            <div className={s.content}>
                <p className={s.text}>{data?.title}</p>
                <div className={s.miscContainer}>
                    <div className={s.date}>Дата публикации: {data?.date}</div>
                    <a href={data?.href} className={s.source}>Источник: {data?.href}</a>
                </div>
            </div>
        </section>
    );
};

export default IdPage;
