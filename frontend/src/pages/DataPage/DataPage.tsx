// import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
// import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
// import { DatePicker } from '@mui/x-date-pickers/DatePicker';
// import { Button } from '@mui/material';
import { newsApi } from '../../services/newsApi';
import { useState } from "react";
import { elasticApi } from "../../services/elasticApi";
import { INews } from "../../models/INews";
import s from './DataPage.module.scss'
import NewsItem from '../../components/NewsItem/NewsItem';


const DataPage = () => {
  const [message, setMessage] = useState<string>('');
  // const [firstValue, setFirstValue] = useState<any>([]);
  // const [secondValue, setSecondValue] = useState<any>([]);

  const {
    data: news,
    error: postgresError,
    isLoading: postgresLoading
  } = newsApi.useGetAllNewsQuery("");

  const [elasticMessage,
    {
      data: newsElastic,
      error: elasticError,
      isLoading: elasticLoading
    }
  ] = elasticApi.usePostElasticDataBySearchMutation();

  // const [elasticMessageDate,
  //   {
  //     data: newsElasticDate,
  //     error: elasticErrorDate,
  //     isLoading: elasticLoadingDate
  //   }
  // ] = elasticApi.usePostElasticDataBySearcWithDateMutation();

  const sendMessage = async () => {
    await elasticMessage(message);
  };

  // const sendData = async () => {
  //   await elasticMessageDate({message, firstValue, secondValue})
  // };

  console.log("News Elastic:", newsElastic);
  // console.log("News Elastic Date:", newsElasticDate);
  console.log("News :", news);


  return (
    <>
      <div className={s.inputContainer}>
        <input
          className={s.searchInput}
          placeholder="Поиск новостей"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          type="text"
        />
        <button className={s.button} onClick={sendMessage}>Искать</button>
      </div>

      {/* <div className={s.dateContainer}>
        <LocalizationProvider dateAdapter={AdapterDayjs}>
          <DatePicker
            label="От"
            value={firstValue}
            onChange={(newValue) => setFirstValue(newValue)}
          />
          <DatePicker
            label="До"
            value={secondValue}
            onChange={(newValue) => setSecondValue(newValue)}
          />
          <Button
            variant="contained"
            color="primary"
            onClick={sendData}
          >
            Искать
          </Button>
        </LocalizationProvider>
      </div> */}

      <div className={s.container}>
        {newsElastic ? (
          <>
            {elasticError && <h1>Ошибка в эластике</h1>}
            {elasticLoading && <h1>Идет загрузка, подождите...</h1>}
            {newsElastic.results?.map((item: INews) => {
              return (
                <NewsItem news={item} key={item.id} />
              )
            })}
          </>
        ) : 
        
        // newsElasticDate ? (
        //   <>
        //     {elasticErrorDate && <h1>Ошибка в БД</h1>}
        //     {elasticLoadingDate && <h1>Идет загрузка, подождите...</h1>}
        //     {newsElasticDate.results?.map((item: INews) => {
        //       return (
        //         <NewsItem news={item} key={item.id} />
        //       )
        //     })}
        //   </>
        // ) : 
        
        (
          <>
            {postgresError && <h1>Ошибка в БД</h1>}
            {postgresLoading && <h1>Идет загрузка, подождите...</h1>}
            {news?.result?.map((item: INews) => {
              return (
                <NewsItem news={item} key={item.id} />
              )
            })}
          </>
        )}

      </div >
    </>
  );
};

export default DataPage;