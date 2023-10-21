import { newsApi } from '../../services/newsApi';
import { useState } from "react";
import { elasticApi } from "../../services/elasticApi";
import { INews } from "../../models/INews";
import { Link } from 'react-router-dom';
import dayjs from 'dayjs';
import s from './DataPage.module.scss'


const DataPage = () => {
  const [message, setMessage] = useState<string>('');

  const {
    data: newsPostgres,
    error: postgresError,
    isLoading: postgresLoading
  } = newsApi.useGetAllNewsQuery("");

  const [elasticMessage,
    {
      data: newsElastic,
      error: elasticError,
      isLoading: elasticLoading
    }
  ] = elasticApi.usePostElasticDataBySearchMutation();

  const sendMessage = async () => {
    await elasticMessage(message)
  }

  return (
    <>
      <div className={s.inputContainer}>
        <input
          className={s.searchInput}
          placeholder="Поиск новостей"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          type="text"
        />
        <button className={s.button} onClick={() => sendMessage()}>Искать</button>
      </div>
      <div className={s.container}>
        {newsElastic ? (
          <>
            {elasticError && <h1>Ошибка в эластике</h1>}
            {elasticLoading && <h1>Идет загрузка, подождите...</h1>}
            {newsElastic?.map((item: INews) => {
              return (
                <Link to={`/data/${item.id}`} className={s.link}>
                  <div key={item.id} className={s.item}>
                    <img src={item.image} alt="img" />
                    <div className={s.title}>{item.title_ru}</div>
                    <div>Дата: {dayjs(item.date).format('DD-MM-YYYY')}</div>
                  </div>
                </Link>
              )
            })}
          </>
        ) : (
          <>
            {postgresError && <h1>Ошибка в БД</h1>}
            {postgresLoading && <h1>Идет загрузка, подождите...</h1>}
            {newsPostgres?.map((item: INews) => {
              return (
                <Link to={`/data/${item.id}`} className={s.link}>
                  <div key={item.id} className={s.item}>
                    <img src={item.image} alt="img" />
                    <div className={s.title}>{item.title_ru}</div>
                    <div>Дата: {dayjs(item.date).format('DD-MM-YYYY')}</div>
                  </div>
                </Link>
              )
            })}
          </>
        )}

      </div >
    </>
  )
}
export default DataPage