import React from "react";
import { MapContainer as Map, GeoJSON } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "./NewsMap.scss";

const NewsMap = ({ countries }) => {
  const countryStyle = {
    fillColor: "white",
    weight: 1,
    color: "black",
    fillOpacity: 1,
  };

  const mapStyle = {
    height: "84vh",  
    display: "flex", 
    alignItems: "stretch"
  };

  const onEachCountry = (country, layer) => {
    layer.options.fillColor = country.properties.color;
    const name = country.properties.ADMIN;
    const text = country.properties.text;
    layer.bindPopup(`<div>${name}</div> <div>${text}</div>`);
  };

  return (
    <Map 
      style={mapStyle} 
      zoom={2} 
      center={[10, 60]}>
      <GeoJSON
        style={countryStyle}
        data={countries}
        onEachFeature={onEachCountry}
      />
    </Map>
  );
};

export default NewsMap;
