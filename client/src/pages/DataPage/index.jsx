import { useState, useEffect } from 'react'
import axios from 'axios'

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
    <div>
      {data.map(card => (
        <div key={card.id}>
          <div>
            Название: {card.title}
          </div>
          <div>
            Ссылка: {card.href}
          </div>
          <div>
            Дата: {card.date}
          </div>
        </div>
      ))
      }
    </div>
  )
}

export default DataPage