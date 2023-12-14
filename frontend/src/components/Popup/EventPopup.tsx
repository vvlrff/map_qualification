import React from "react";
import Popup from "reactjs-popup";

interface NewsPopupProps {
  id: number,
  title_en: string,
  title_ru: string,
  date: string,
  href: string,
  image: any,
  country: string[],
  city: string[],
  topical_keywords: string[]
  onClose: () => void;
}

const EventPopup: React.FC<NewsPopupProps> = ({ id, title_en, title_ru, date, href, country, image, city, topical_keywords, onClose }) => {
  const popupStyle = {
    content: {
      background: "#ffffff",
      borderRadius: "10px",
      boxShadow: "0 0 10px rgba(0, 0, 0, 0.2)",
      padding: "20px",
    },
    overlay: {
      background: "rgba(0, 0, 0, 0.5)",
    },
  };

  return (
    <Popup open={true} closeOnDocumentClick onClose={onClose} contentStyle={popupStyle.content} overlayStyle={popupStyle.overlay}>
      <div>
        <h3>{title_ru}</h3>
        <p>title_en: {title_en}</p>
        <p>href: {href}</p>

        <img src={image} alt="img" />
        <div>Страны: {country.length > 1 ? (
          <span>
            {country.map(country_item => (
              <span> {country_item}</span>
            ))}
          </span>
        ) : (
          <span>
            {country}
          </span>
        )}</div>
        <p>topical_keywords: {topical_keywords}</p>
        <p>date: {date.toLocaleString()}</p>
        <button onClick={onClose}>Закрыть</button>
      </div>
    </Popup>
  );
};

export default EventPopup;
