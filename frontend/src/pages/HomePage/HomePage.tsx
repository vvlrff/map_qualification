import { Link } from "react-router-dom"
import s from "./HomePage.module.scss"
import mapLogo from '../../assets/images/icons8-google-карты.svg'
import dataLogo from "../../assets/images/free-icon-database-storage-5655041.png"
import calendarLogo from "../../assets/images/free-icon-calendar-2838764.png"
import { newsApi } from "../../services/newsApi"

const HomePage = () => {

  const [collect, { isLoading }] = newsApi.useCollectNewsMutation();

  const collectNews = async () => {
    await collect('');
  };

  return (
    <div>
      {isLoading &&
        <div className={s.overlay}>
          <div className={s.loadingMessage}>
            Идет сбор информации, подождите
            <span
              style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
              }}
            >
              <div className="spinner-grow text-success" role="status"></div>
              <div className="spinner-grow text-danger" role="status"></div>
              <div className="spinner-grow text-info" role="status"></div>
            </span>
          </div>
        </div>
      }

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

        <div className={s.link} onClick={() => collectNews()}>
          <div className={s.lower_block}>
            <div className={s.text}>
              Собрать данные
            </div>
            <img src={calendarLogo} className={s.calendarLogo} alt="Логотип календаря"></img>
          </div>
        </div>
      </div>
    </div >
  );
};

export default HomePage;

