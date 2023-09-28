import { useState, useEffect } from 'react';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { Button, Container } from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import dayjs from 'dayjs';

const MuiDateRangePicker = () => {
    const [firstValue, setFirstValue] = useState([]);
    const [secondValue, setSecondValue] = useState([]);
    const [serverResponse, setServerResponse] = useState(null);

    const navigate = useNavigate();

    useEffect(() => {
        if (serverResponse) {
            navigate("/calendar/data", { state: { response: serverResponse } });
        }
    }, [serverResponse, navigate]);

    const sendData = () => {
        console.log(firstValue.$d)
        console.log(secondValue.$d)

        const formattedFirstValue = dayjs(firstValue.$d).format('DD-MM-YYYY')
        const formattedSecondValue = dayjs(secondValue.$d).format('DD-MM-YYYY')

        console.log(formattedFirstValue)
        console.log(formattedSecondValue)
        axios
            .get(`http://127.0.0.1:8000/classification/news/${formattedFirstValue}/${formattedSecondValue}`)
            .then((res) => {
                console.log(res.data);
                setServerResponse(res.data)
            })
            .catch((error) => {
                console.log(error);
            });
    };

    return (
        <LocalizationProvider dateAdapter={AdapterDayjs}>
            <Container components={['DatePicker', 'DatePicker']}>
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
            </Container>
        </LocalizationProvider>
    );
}

export default MuiDateRangePicker

