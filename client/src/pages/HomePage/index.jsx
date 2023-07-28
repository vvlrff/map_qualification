import axios from 'axios'
import { useState } from 'react'


const HomePage = () => {

  const [data, setData] = useState([])

  const collectData = () => {
    axios
      .get('http://127.0.0.1:8000/collection/get_news')
      .then(res => {
        console.log(res.data)
        setData(res.data)
      })
      .catch(err => {
        console.log(err);
      })
  }

  return (
    <div>
      <div>
        <div>Собрать данные</div>
        <button onClick={collectData}>Собрать данные</button>
      </div>
      <div>
        <div>Очистить базу</div>
        
      </div>
      <div>
        <div>Выбрать данные во временном промежутке</div>
      </div>
    </div>
  )
}

export default HomePage