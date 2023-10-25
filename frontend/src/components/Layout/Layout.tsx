import { Outlet } from 'react-router-dom'
import Sidebar from '../Sidebar/Sidebar'

const Layout = () => {
  return (
    <>
      <Sidebar />
      <Outlet />
    </>
  )
}

export default Layout