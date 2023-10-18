import { Link } from "react-router-dom"
import dayjs from 'dayjs';
import s from './DataPage.module.scss'
import { newsApi } from '../../services/newsApi';


const DataPage = () => {
  const {
    data: news,
  } = newsApi.useGetAllNewsQuery('');

  return (
    <div className={s.container}>
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