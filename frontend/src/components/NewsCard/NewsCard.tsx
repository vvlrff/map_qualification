import React from 'react';
import dayjs from 'dayjs';
import s from './NewsCard.module.scss';

interface NewsCardProps {
  item: {
    id: number;
    title_ru: string;
    date: string;
  };
  onClose: () => void;
}

const NewsCard: React.FC<NewsCardProps> = ({ item, onClose }) => {
  return (
    <div className={s.newsCard}>
      <div className={s.closeButton} onClick={onClose}>
        Закрыть
      </div>
      <div className={s.title}>{item.title_ru}</div>
      <div>Дата: {dayjs(item.date).format('DD-MM-YYYY')}</div>
    </div>
  );
};

export default NewsCard;