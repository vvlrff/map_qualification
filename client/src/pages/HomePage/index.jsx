// import { useNavigate } from 'react-router-dom'
// import MuiDateRangePicker from '../../components/MuiDateRangePicker'
// import { collectData, deleteData } from './HomePageData'
import { Link } from "react-router-dom"

import s from "./HomePage.module.scss"

import mapLogo from '../../assets/images/icons8-google-карты.svg'
import dataLogo from "../../assets/images/free-icon-database-storage-5655041.png"
import calendarLogo from "../../assets/images/free-icon-calendar-2838764.png"
const HomePage = () => {
  // const navigate = useNavigate()

  // const handleCollectData = async () => {
  //   await collectData()
  //   navigate('data')
  // }

  return (
    <div className={s.container}>
      <Link to="/data">
        <div className={s['left-block']}>
          <div className={s.text}>
            Просмотреть все данные
          </div>
          <img src={dataLogo} className={s.dataLogo} alt="Логотип бд"></img>
        </div>
      </Link>

      <Link to="/map">
        <div className={s['right-block']}>
          <div className={s.text}>
            Карта
          </div>
          <img src={mapLogo} className={s.mapLogo} alt="Логотип карты"></img>
        </div>
      </Link>

      <Link to="/calendar">
        <div className={s['lower-block']}>
          <div className={s.text}>
            Данные по временному промежутку
          </div>
          <img src={calendarLogo} className={s.calendarLogo} alt="Логотип календаря"></img>
        </div>
      </Link>

      {/* <div className={s.space}>
        <button onClick={handleCollectData}>Собрать данные</button>
        <button onClick={deleteData}>Удалить данные</button>

        <div>
          <MuiDateRangePicker />
        </div>
      </div> */}

    </div>
  )
}

export default HomePage

