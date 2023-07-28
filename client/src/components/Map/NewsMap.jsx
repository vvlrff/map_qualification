import React from "react";
import { MapContainer as Map, GeoJSON } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "./NewsMap.css";

const NewsMap = ({ countries }) => {
  const mapStyle = {
    fillColor: "white",
    weight: 1,
    color: "black",
    fillOpacity: 1,
  };

  const onEachCountry = (country, layer) => {
    layer.options.fillColor = country.properties.color;
    const name = country.properties.ADMIN;
    const text = country.properties.text;
    layer.bindPopup(`<div>${name}</div> <div>${text}</div>`);
  };

  return (
    <Map style={{ height: "90vh" }} zoom={2} center={[10, 60]}>
      <GeoJSON
        style={mapStyle}
        data={countries}
        onEachFeature={onEachCountry}
      />
    </Map>
  );
};

export default NewsMap;
