import { Link } from "react-router-dom"
import dayjs from 'dayjs';
import s from './DataPage.module.scss'
import { newsApi } from '../../services/newsApi';
import { useState } from "react";


const DataPage = () => {
  const [message, setMessage] = useState<string>('');
  
  const {
    data: news,
  } = newsApi.useGetAllNewsQuery(message);

  return (
    <div className={s.container}>
      <input
        className={s.searchInput}
        placeholder="Поиск новостей"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        type="text"
      />
      {news?.map((item) => {
        return (
          <Link to={`/data/${item.id}`} className={s.link}>
            <div key={item.id} className={s.item}>
              <div className={s.title}>
                {item.title}
              </div>
              <div>
                Дата: {dayjs(item.date).format('DD-MM-YYYY')}
              </div>
            </div>
          </Link>
        );
      })}
    </div>
  )
}
export default DataPage