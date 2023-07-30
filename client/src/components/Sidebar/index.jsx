import React, { useState } from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import { Link } from 'react-router-dom';
import { SidebarData } from './SidebarData';
import s from  './Sidebar.module.scss';
import { IconContext } from 'react-icons';

function Navbar() {
  const [sidebar, setSidebar] = useState(false);

  const showSidebar = () => setSidebar(!sidebar);

  return (
    <>
      <IconContext.Provider value={{ color: '#fff' }}>
        <div className={s.navbar}>
          <Link to='#' className={s['menu-bars']}>
            <FaIcons.FaBars onClick={showSidebar} />
          </Link>
        </div>
        <nav className={sidebar ? s['nav-menu'] + ' ' + s.active : s['nav-menu']}>.
          <ul className={s['nav-menu-items']} onClick={showSidebar}>
            <li className={s['navbar-toggle']}>
              <Link to='#' className={s['menu-bars']}>
                <AiIcons.AiOutlineClose />
              </Link>
            </li>
            {SidebarData.map((item, index) => {
              return (
                <li key={index} className={s['nav-text']}>
                  <Link to={item.path}>
                    {item.icon}
                    <span className={s.span}>{item.title}</span>
                  </Link>
                </li>
              );
            })}
          </ul>
        </nav>
      </IconContext.Provider>
    </>
  );
}

export default Navbar;
