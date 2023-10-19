import { MapContainer as Map, GeoJSON } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "./NewsMap.scss";

interface CountryFeature {
  type: string;
  properties: {
    ADMIN: string;
    color: string; 
    text: string;
  };
}

interface NewsMapProps {
  countries: CountryFeature[];
}

const NewsMap: React.FC<NewsMapProps> = ({ countries }) => {
  const countryStyle = {
    fillColor: "white",
    weight: 1,
    color: "black",
    fillOpacity: 1,
  };

  const mapStyle: React.CSSProperties = {
    height: "calc(90vh - 80px)",
    display: "flex",
    alignItems: "stretch",
  };

  const onEachCountry = (country: CountryFeature, layer: L.Layer) => {
    layer.options.fillColor = country.properties.color;
    const name = country.properties.ADMIN;
    const text = country.properties.text;
    layer.bindPopup(`<div style="font-weight: bold;">${name}</div> <div>${text}</div>`);
  };

  return (
    <Map
      style={mapStyle}
      zoom={2}
      center={[45, 0]}
    >
      <GeoJSON
        style={countryStyle}
        data={countries}
        onEachFeature={onEachCountry}
      />
    </Map>
  );
};

export default NewsMap;