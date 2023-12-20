import { useParams } from "react-router-dom";
import { newsApi } from "../../services/newsApi";
import s from "./IdPage.module.scss";


const IdPage = () => {
    const { id } = useParams();
    const numberId = Number(id);
    console.log("numberId", numberId)

    const { data } = newsApi.useGetNewsByIdQuery(numberId);

    console.log(data)

    return (
        <section className={s.section}>
            <img src={data?.result?.image} className={s.img} alt="articlePhoto" />
            <div className={s.content}>
                <p className={s.text}>{data?.result?.title_ru}</p>
                <p className={s.text}>{data?.result?.title_en}</p>
                <div>Страны: {data?.result?.country.length > 1 ? (
                    <span>
                        {data?.result?.country.map((country: any) => (
                            <span> {country}</span>
                        ))}
                    </span>
                ) : (
                    <span>
                        {data?.result?.country}
                    </span>
                )}</div>
                <div>Города: {data?.result?.city}</div>
                <div className={s.miscContainer}>
                    <div className={s.date}>Дата публикации: {data?.result?.date}</div>
                    <a href={data?.result?.href} className={s.source}>Источник: {data?.result?.href}</a>
                </div>
            </div>
        </section>
    );
};

export default IdPage;
