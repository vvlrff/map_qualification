import React, { useState } from 'react';
import dayjs from 'dayjs';
import MyMap from '../../components/Map/MyMap';
import { newsApi } from '../../services/newsApi';
import { INews } from '../../models/INews';
import EventPopup from '../../components/Popup/EventPopup';
import s from './MapPage.module.scss';


const MapPage: React.FC = () => {
  const [selectedEvent, setSelectedEvent] = useState<INews | null>(null);

  const { data: news } = newsApi.useGetAllNewsQuery('');

  const closeEventPopup = () => {
    setSelectedEvent(null);
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
                  onClick={() => setSelectedEvent(item)}
                >
                  <div className={s.title}>{item.title_ru}</div>
                  <div>Дата: {dayjs(item.date).format('DD-MM-YYYY')}</div>
                </div>
              );
            })}
          </>
        ) : null}
      </div>

      <div className={s.map}>
        <MyMap />
      </div>

      {selectedEvent && (
        <EventPopup
          id={selectedEvent.id}
          title_en={selectedEvent.title_en}
          title_ru={selectedEvent.title_ru}
          date={selectedEvent.date}
          href={selectedEvent.href}
          country={selectedEvent.country}
          image={selectedEvent.image}
          city={selectedEvent.city}
          topical_keywords={selectedEvent.topical_keywords}
          onClose={closeEventPopup}
        />
      )}

    </div>
  );
};

export default MapPage;