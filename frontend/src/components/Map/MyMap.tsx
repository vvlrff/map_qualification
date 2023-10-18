import { useState, useEffect } from "react";
import Loading from "./Loading";
import NewsMap from "./NewsMap";
import LoadCountriesTask from "../../tasks/LoadCountriesTask";
import Legend from "./Legend";

const MyMap = () => {
  const [countries, setCountries] = useState<any>([]);

  const load = () => {
    const loadCountriesTask = new LoadCountriesTask();
    loadCountriesTask.load((countries: any) => setCountries(countries));
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
          <Legend />
        </div>
      )}
    </div>
  );
};

export default MyMap;