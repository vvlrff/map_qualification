import legendItems from "../entities/LegendItems";
import countriesData from "../data/countries.json";

class LoadCountryTask {
  url = "http://127.0.0.1:8000/classification/countries_coordinates";

  setState = null;
  

  load = async (setState) => {
    this.setState = setState;

    let response = await fetch(this.url);

    let data = await response.json();

    this.processData(data)

  };

  processData = (newsCountries) => {
    console.log(newsCountries);
    for (let i = 0; i < countriesData.features.length; i++) {
      const country = countriesData.features[i];

      let textData = [];

      for (let j = 0; j < newsCountries.length; j++) {
        if (newsCountries[j].country === country.properties.ADMIN) {
          textData.push(newsCountries[j].text)
        }
      }
      
      country.properties.text = textData;

      this.setCountryColor(country);
    }
    this.setState(countriesData.features);
  };

  setCountryColor = (country) => {
    const legendItem = legendItems.find((item) =>
      item.isFor(country.properties.text.length)
    );

    if (legendItem != null) country.properties.color = legendItem.color;
  };
}

export default LoadCountryTask;
