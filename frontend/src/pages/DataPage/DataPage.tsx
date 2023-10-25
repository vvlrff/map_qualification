import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { Button } from '@mui/material';
import { newsApi } from '../../services/newsApi';
import { useState } from "react";
import { elasticApi } from "../../services/elasticApi";
import { INews } from "../../models/INews";
import NewsItem from '../../components/NewsItem/NewsItem';
import s from './DataPage.module.scss'


const DataPage = () => {
  const [message, setMessage] = useState<string>('');
  const [firstValue, setFirstValue] = useState<any>([]);
  const [secondValue, setSecondValue] = useState<any>([]);

  const {
    data: newsPostgres,
    error: postgresError,
    isLoading: postgresLoading
  } = newsApi.useGetAllNewsQuery("");

  const [
    elasticMessage,
    { data: newsElastic, error: elasticError, isLoading: elasticLoading }
  ] = elasticApi.usePostElasticDataBySearchMutation();

  const [
    elasticMessageDate,
    {
      data: newsElasticDate,
      error: elasticErrorDate,
      isLoading: elasticLoadingDate
    }
  ] = elasticApi.usePostElasticDataBySearcWithDateMutation();

  const sendMessage = async () => {
    await elasticMessage(message);
  };

  const sendData = async () => {
    await elasticMessageDate({ message, firstValue, secondValue });
  };

  const getNewsToRender = () => {
    if (newsElastic) {
      return { data: newsElastic, error: elasticError, loading: elasticLoading };
    } else if (newsElasticDate) {
      return { data: newsElasticDate, error: elasticErrorDate, loading: elasticLoadingDate };
    } else {
      return { data: newsPostgres, error: postgresError, loading: postgresLoading };
    }
  };

  const { data, error, loading } = getNewsToRender();

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
        <button className={s.button} onClick={sendMessage}>
          Искать
        </button>
      </div>

      <div className={s.dateContainer}>
        <LocalizationProvider dateAdapter={AdapterDayjs}>
          <DatePicker label="От" value={firstValue} onChange={(newValue) => setFirstValue(newValue)} />
          <DatePicker label="До" value={secondValue} onChange={(newValue) => setSecondValue(newValue)} />
          <Button variant="contained" color="primary" onClick={sendData}>
            Искать
          </Button>
        </LocalizationProvider>
      </div>

      <div className={s.container}>
        {data ? (
          <>
            {error && <h1>Ошибка</h1>}
            {loading ? <h1>Идет загрузка, подождите...</h1> : null}
            {data.result?.map((item: INews) => (
              <NewsItem news={item} key={item.id} />
            ))}
          </>
        ) : null}
      </div>
    </>
  );
};

export default DataPage;