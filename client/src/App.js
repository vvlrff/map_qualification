import { Route, createBrowserRouter, RouterProvider, createRoutesFromElements } from 'react-router-dom';

import Layout from "./components/Layout";

import HomePage from './pages/HomePage';
import DataPage from './pages/DataPage';
import MapPage from './pages/MapPage';
import IdPage from './pages/IdPage';
import NotFoundPage from './pages/NotFoundPage';



const router = createBrowserRouter(createRoutesFromElements(
  <Route path='/' element={<Layout />} >
    <Route index element={<HomePage />} />
    <Route path='map' element={<MapPage />} />
    <Route path='data' element={<DataPage />} />
    <Route path='data/:id' element={<IdPage />} />
    <Route path='*' element={<NotFoundPage />} />
  </Route>
))

function App() {
  return (
      <RouterProvider router={router} />
  )
}

export default App;