import React, { useContext, useState } from 'react';
import { Link } from "react-router-dom";
import { ThemeContext } from '../../Context/ThemeContext';
// import Login from './Login';

function NavBar  () {
  const themeContext = useContext(ThemeContext);

  const {isLightTheme, light, dark} = themeContext;

  const theme = isLightTheme ? light : dark;
  return (
    <nav style={{ background:theme.ui, color:theme.syntax}}className="fixed w-full bg-green-400 py-4">
      <div className="container mx-auto flex justify-between items-center rounded-lg">
        <div className="text-white font-bold text-xl">
          <Link to="/">Ralphy Boy</Link>
        </div>
        <ul className="flex space-x-4 text-white">
          <div className='rounded 3xl bg-slate-800'>
          <li>
            <Link to="/Login" className="hover:text-gray-400">
              Login
            </Link>
          </li>
          </div>
        </ul>
      </div>
    </nav>
  );
};

export default NavBar;
