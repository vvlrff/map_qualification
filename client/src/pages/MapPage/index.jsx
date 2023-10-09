import React from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios' 

import s from "./MapPage.module.scss"

import MyMap from '../../components/Map/MyMap'

const MapPage = () => {
  const navigate = useNavigate()

  const collectData = () => {
    axios
      .get('http://127.0.0.1:8000/collection/get_countries')

    window.location.reload();
  }

  return (
    <>
      <button className={s.button1} onClick={collectData}>Собрать данные</button>
      <button className={s.button} onClick={() => navigate('/')}>Вернуться назад</button>
      <MyMap />
    </>
  )
}

export default MapPage