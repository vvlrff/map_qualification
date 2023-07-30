import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import s from "./HomePage.module.scss"

const HomePage = () => {
  const navigate = useNavigate()

  const collectData = () => {
    axios
      .get('http://127.0.0.1:8000/collection/get_news')
      .then(res => {
        console.log(res.data)
      })
      .catch(err => {
        console.log(err);
      })

    let path = `data`;
    navigate(path);

  }

  const deleteData = () => {
    axios
      .get('http://127.0.0.1:8000/delete/news')
      .then(res => {
        console.log(res.data)
      })
      .catch(err => {
        console.log(err);
      })

    alert("Данные успешно удалены")
  }
  
  return (
    <div className={s.container}>
      <div>
        <button onClick={collectData}>Собрать данные</button>
      </div>
      <div>
        <button onClick={deleteData}>Удалить данные</button>
      </div>
      <div>
        <div>Выбрать данные во временном промежутке</div>
      </div>
    </div>
  )
}

export default HomePage