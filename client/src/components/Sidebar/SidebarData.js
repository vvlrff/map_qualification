import React from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';

export const SidebarData = [
  {
    title: 'Главная',
    path: '/',
    icon: <AiIcons.AiFillHome />
  },
  {
    title: 'Карта',
    path: '/map',
    icon: <FaIcons.FaMap />
  },
  {
    title: 'Данные',
    path: '/data',
    icon: <IoIcons.IoIosPaper />
  }
];
