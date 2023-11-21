import { useState, useEffect } from "react";

import NewsMap from "./NewsMap";
import LoadCountriesTask from "../../tasks/LoadCountriesTask";
import Legend from "./Legend";

const MyMap = () => {
  const [countries, setCountries] = useState<any>([]);

  const load = () => {
    const loadCountriesTask = new LoadCountriesTask();
    loadCountriesTask.load((countries: any) => setCountries(countries));
  };

  useEffect(() => {
    setTimeout(load, 2)
  }, [countries]);
  console.log(countries)

  return (
    <>
      {countries.length === 0 ? (
        // <Loading />
        <div>Идет загрузка</div>
      ) : (
        <>
          <NewsMap countries={countries} />
          <Legend />
        </>
      )}
    </>
  );
};

export default MyMap;