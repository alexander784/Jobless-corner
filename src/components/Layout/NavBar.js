import React from 'react';
import { Link } from "react-router-dom";

const NavBar = () => {
  return (
    <div className='navbar bg-gray-800 text-black p-4'>
      <Link to="/" className='logo text-black'>
        Lexa
      </Link>
      <div className='space-x-4'>
        <Link to="/" style={{ textDecoration: 'none', color: 'black' }}>Home</Link>
        <Link to="/" style={{ textDecoration: 'none', color: 'black' }}>Interviews</Link>
      </div>
    </div>
  );
};

export default NavBar;
