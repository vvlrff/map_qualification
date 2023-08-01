import { useNavigate } from 'react-router-dom'
import MuiDateRangePicker from '../../components/MuiDateRangePicker'
import { collectData, deleteData } from './HomePageData'
import s from "./HomePage.module.scss"


const HomePage = () => {
  const navigate = useNavigate()

  const handleCollectData = async () => {
    await collectData()
    navigate('data')
  }


  return (
    <div className={s.container}>
      <div>
        <button onClick={handleCollectData}>Собрать данные</button>
      </div>
      <div>
        <button onClick={deleteData}>Удалить данные</button>
      </div>
      <div>
        <MuiDateRangePicker />
      </div>
    </div>
  )
}

export default HomePage