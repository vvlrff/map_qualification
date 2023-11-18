import { Link } from "react-router-dom"
import s from "./HomePage.module.scss"
import mapLogo from '../../assets/images/icons8-google-карты.svg'
import dataLogo from "../../assets/images/free-icon-database-storage-5655041.png"

const HomePage = () => {
  return (
    <div className={s.container}>
      <Link to="/data" className={s.link}>
        <div className={s.block}>
          <div className={s.text}>
            Данные
          </div>
          <img src={dataLogo} className={s.logo} alt="Логотип бд"></img>
        </div>
      </Link>

      <Link to="/map" className={s.link}>
        <div className={s.block}>
          <div className={s.text}>
            Карта
          </div>
          <img src={mapLogo} className={s.logo} alt="Логотип карты"></img>
        </div>
      </Link>
    </div>
  );
};

export default HomePage;

