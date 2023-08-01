import React, { useState, useEffect } from "react";

import Loading from "./Loading";
import NewsMap from "./NewsMap";
import LoadCountriesTask from "../../tasks/LoadCountriesTask";
import Legend from "./Legend";
import legendItems from "../../entities/LegendItems";

const MyMap = () => {
  const [countries, setCountries] = useState([]);

  const legendItemsReverse = [...legendItems].reverse();

  const load = () => {
    const loadCountriesTask = new LoadCountriesTask();
    loadCountriesTask.load((countries) => setCountries(countries));
  };

  useEffect(load, [countries]);
  console.log(countries)
  return (
    <div>
      {countries.length === 0 ? (
        <Loading />
      ) : (
        <div>
          <NewsMap countries={countries} />
          <Legend legendItems={legendItemsReverse} />
        </div>
      )}
    </div>
  );
};

export default MyMap;