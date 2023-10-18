import { useState } from 'react';
import * as FaIcons from 'react-icons/fa';
import * as IoIcons from 'react-icons/io';
import * as AiIcons from 'react-icons/ai';
import { Link } from 'react-router-dom';
import s from './Sidebar.module.scss';
import { IconContext } from 'react-icons';

function Navbar() {
  const [sidebar, setSidebar] = useState(false);

  const showSidebar = () => setSidebar(!sidebar);

  return (
    <>
      <IconContext.Provider value={{ color: '#fff' }}>

        <div className={s.navbar}>
          <Link to='#' className={s.menu_bars}>
            <FaIcons.FaBars onClick={showSidebar} />
          </Link>
        </div>

        <nav className={sidebar ? s.nav_menu + ' ' + s.active : s.nav_menu}>.
          <ul className={s.nav_menu_items} onClick={showSidebar}>

            <li className={s.navbar_toggle}>
              <Link to='#' className={s.menu_bars}>
                <AiIcons.AiOutlineClose />
              </Link>
            </li>

            <li className={s.nav_text}>
              <Link to='/'>
                <AiIcons.AiFillHome />
                <span className={s.span}>Главная</span>
              </Link>
            </li>

            <li className={s.nav_text}>
              <Link to='/map'>
                <FaIcons.FaMap />
                <span className={s.span}>Карта</span>
              </Link>
            </li>

            <li className={s.nav_text}>
              <Link to='/data'>
                <IoIcons.IoIosPaper />
                <span className={s.span}>Данные</span>
              </Link>
            </li>

          </ul>
        </nav>
      </IconContext.Provider>
    </>
  );
}

export default Navbar;
