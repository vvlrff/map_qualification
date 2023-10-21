import { Route, createBrowserRouter, RouterProvider, createRoutesFromElements } from 'react-router-dom';
import Layout from "./components/Layout";
import HomePage from './pages/HomePage/HomePage';
import DataPage from './pages/DataPage/DataPage';
import MapPage from './pages/MapPage/MapPage';
import IdPage from './pages/IdPage/IdPage';
import NotFoundPage from './pages/NotFoundPage/NotFoundPage';
import CalendarPage from './pages/CalendarPage/CalendarPage';
import CalendarDataPage from './pages/CalendarDataPage/CalendarDataPage';


const router = createBrowserRouter(createRoutesFromElements(
  <Route path='/' element={<Layout />} >
    <Route index element={<HomePage />} />
    <Route path='map' element={<MapPage />} />
    <Route path='data' element={<DataPage />} />
    <Route path='data/:id' element={<IdPage />} />
    <Route path='calendar' element={<CalendarPage />} />
    <Route path='calendar/data' element={<CalendarDataPage />} />
    <Route path='*' element={<NotFoundPage />} />
  </Route>
))

function App() {
  return (
      <RouterProvider router={router} />
  )
}

export default App;
