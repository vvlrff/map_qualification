import React, { useState } from 'react';
import dayjs from 'dayjs';
import MyMap from '../../components/Map/MyMap';
import { newsApi } from '../../services/newsApi';
import NewsCard from '../../components/NewsCard/NewsCard';
import s from './MapPage.module.scss';
import { INews } from '../../models/INews';

const MapPage: React.FC = () => {
  const { data: news } = newsApi.useGetAllNewsQuery('');
  const [selectedItem, setSelectedItem] = useState<any>(null);

  const handleOpenCard = (item: any) => {
    setSelectedItem(item);
  };

  const handleCloseCard = () => {
    setSelectedItem(null);
  };

  return (
    <div className={s.container}>

      <div className={s.sidebar}>

        {news ? (
          <>
            {news.result?.map((item: INews) => {
              return (
                <div
                  key={item.id}
                  className={s.item}
                  onClick={() => handleOpenCard(item)}
                >
                  <div className={s.title}>{item.title_ru}</div>
                  <div>Дата: {dayjs(item.date).format('DD-MM-YYYY')}</div>
                </div>
              );
            })}
          </>
        ) : null}

        {/* {
          news?.map((item: INews) => {
            return (
              <div
                key={item.id}
                className={s.item}
                onClick={() => handleOpenCard(item)}
              >
                <div className={s.title}>{item.title_ru}</div>
                <div>Дата: {dayjs(item.date).format('DD-MM-YYYY')}</div>
              </div>
            );
          })
        } */}
      </div>



      <div className={s.map}>
        <MyMap />
      </div>

      {selectedItem && (
        <div className={s.overlay}>
          <NewsCard item={selectedItem} onClose={handleCloseCard} />
        </div>
      )}

    </div>
  );
};

export default MapPage;