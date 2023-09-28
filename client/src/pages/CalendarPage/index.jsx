import s from './CalendarPage.module.scss'
import MuiDateRangePicker from '../../components/MuiDateRangePicker';


const CalendarPage = () => {
  return (
    <div className={s.container}>
      <MuiDateRangePicker />
    </div>
  )
}
export default CalendarPage