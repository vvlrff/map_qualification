import { useState, useEffect } from 'react'
import { Link } from "react-router-dom"
import axios from 'axios'
import dayjs from 'dayjs';
import s from './DataPage.module.scss'


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
          <Link to={`/data/${item.id}`} className={s.link}>
            <div key={index} className={s.item}>
              <div className={s.title}>
                {item.title}
              </div>
              {/* <div>
                Ссылка: {item.href}
              </div> */}
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