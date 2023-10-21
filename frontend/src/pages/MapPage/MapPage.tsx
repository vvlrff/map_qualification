import dayjs from 'dayjs';
import MyMap from '../../components/Map/MyMap'
import { newsApi } from '../../services/newsApi';
import s from "./MapPage.module.scss"

const MapPage = () => {
  const {
    data: news,
  } = newsApi.useGetAllNewsQuery('');

  return (
    <div className={s.container}>
      <div className={s.sidebar}>
        {news?.map((item) => {
          return (
            <div key={item.id} className={s.item}>
              <div className={s.title}>
                {item.title_ru}
              </div>
              <div>
                Дата: {dayjs(item.date).format('DD-MM-YYYY')}
              </div>
            </div>
          );
        })}
      </div>
      <div className={s.map}>
        <MyMap />
      </div>
    </div>
  )
}

export default MapPage