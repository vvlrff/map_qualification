import React from 'react'
import { useNavigate } from 'react-router-dom'
import s from "./MapPage.module.scss"

import MyMap from '../../components/Map/MyMap'

const MapPage = () => {
  const navigate = useNavigate()

  return (
    <>
      <button className={s.button} onClick={() => navigate(-1)}>Вернуться назад</button>
      <MyMap />
    </>
  )
}

export default MapPage