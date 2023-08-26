import axios from "axios";


export const collectData = () => {
    axios
        .get('http://127.0.0.1:8000/collection/get_news')
        .then(res => {
            console.log(res.data)
        })
        .catch(err => {
            console.log(err);
        })
}

export const deleteData = () => {
    axios
        .get('http://127.0.0.1:8000/delete/news')
        .then(res => {
            console.log(res.data)
        })
        .catch(err => {
            console.log(err);
        })

    alert("Данные успешно удалены")
}