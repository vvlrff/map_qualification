import { useNavigate } from 'react-router-dom'
import MyMap from '../../components/Map/MyMap'
import s from "./MapPage.module.scss"

const MapPage = () => {
  const navigate = useNavigate()

  return (
    <>
      <button className={s.button} onClick={() => navigate('/')}>Вернуться назад</button>
      <MyMap />
    </>
  )
}

export default MapPage