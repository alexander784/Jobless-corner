import React, { useState } from 'react';
import { Link } from "react-router-dom";
import Login from './Login';

const NavBar = () => {
  return (
    <nav className="fixed w-full bg-green-400 py-4">
      <div className="container mx-auto flex justify-between items-center rounded-lg">
        <div className="text-white font-bold text-xl">
          <Link to="/">Crabs</Link>
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
