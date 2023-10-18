import { useLocation } from "react-router-dom";
import { Link } from "react-router-dom"
import dayjs from 'dayjs';

import s from './CalendarPage.module.scss'


const CalendarPage = () => {
  const location = useLocation();
  const { state } = location;

  console.log("state.response", state.response);

  return (
    <div className={s.container}>
      {state.response.map((item: any) => {
        return (
          <Link to={`/data/${item.id}`} className={s.link}>
            <div key={item.title} className={s.item}>
              <div className={s.title}>
                {item.title}
              </div>
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
export default CalendarPage