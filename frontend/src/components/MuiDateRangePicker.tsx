import { useState } from 'react';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import dayjs from 'dayjs';

const MuiDateRangePicker = () => {
    const [firstValue, setFirstValue] = useState<any>([]);
    const [secondValue, setSecondValue] = useState<any>([]);
    // const [serverResponse, setServerResponse] = useState(null);

    const navigate = useNavigate();

    // useEffect(() => {
    //     if (serverResponse) {
    //         navigate("/calendar/data", { state: { response: serverResponse } });
    //     }
    // }, [serverResponse, navigate]);

    const sendData = () => {
        console.log(firstValue)
        console.log(secondValue)

        const formattedFirstValue = dayjs(firstValue).format('DD-MM-YYYY')
        const formattedSecondValue = dayjs(secondValue).format('DD-MM-YYYY')

        console.log(formattedFirstValue)
        console.log(formattedSecondValue)
        // axios
        //     .get(`http://127.0.0.1:8000/classification/news/${formattedFirstValue}/${formattedSecondValue}`)
        //     .then((res) => {
        //         console.log(res.data);
        //         setServerResponse(res.data)
        //     })
        //     .catch((error) => {
        //         console.log(error);
        //     });
    };

    return (
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
    );
}

export default MuiDateRangePicker

