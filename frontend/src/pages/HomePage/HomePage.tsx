import { Link } from "react-router-dom"
import s from "./HomePage.module.scss"
import mapLogo from '../../assets/images/icons8-google-карты.svg'
import dataLogo from "../../assets/images/free-icon-database-storage-5655041.png"
import calendarLogo from "../../assets/images/free-icon-calendar-2838764.png"

const HomePage = () => {
  return (
    <div className={s.container}>
      <Link to="/data" className={s.link}>
        <div className={s.left_block}>
          <div className={s.text}>
            Просмотреть все данные
          </div>
          <img src={dataLogo} className={s.dataLogo} alt="Логотип бд"></img>
        </div>
      </Link>

      <Link to="/map" className={s.link}>
        <div className={s.right_block}>
          <div className={s.text}>
            Карта
          </div>
          <img src={mapLogo} className={s.mapLogo} alt="Логотип карты"></img>
        </div>
      </Link>

      <div className={s.link}>
        <div className={s.lower_block}>
          <div className={s.text}>
            Собрать данные
          </div>
          <img src={calendarLogo} className={s.calendarLogo} alt="Логотип календаря"></img>
        </div>
      </div>
    </div>
  )
}

export default HomePage

