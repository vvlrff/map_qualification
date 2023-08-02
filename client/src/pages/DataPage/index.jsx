import { useState, useEffect } from 'react'
import axios from 'axios'
import s from './DataPage.module.scss'
import dayjs from 'dayjs';

const DataPage = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/classification/news_guardian`)
      .then(res => {
        setData(res.data)
      })
      .catch(err => {
        console.log(err);
      })
  })

  return (
    <div className={s.container}>
      {data.map((item, index) => {
        return (
          <div key={index} className={s.item}>
            <div>
              Название: {item.title}
            </div>
            <div>
              Ссылка: {item.href}
            </div>
            <div>
              Дата: {dayjs(item.date).format('DD-MM-YYYY')}
            </div>
          </div>
        );
      })}
    </div>
  )
}
export default DataPage