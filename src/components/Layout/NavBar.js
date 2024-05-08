import React from 'react';
import { Link } from "react-router-dom";

const NavBar = () => {
  return (
    <nav className="fixed w-full bg-zinc-300 py-4">
      <div className="container mx-auto flex justify-between items-center rounded-lg">
        <div className="text-white font-bold text-xl">
          <Link to="/">Crabs</Link>
        </div>
        <ul className="flex space-x-4 text-white">
          <li>
            <Link to="/" className="hover:text-gray-400">
              Home
            </Link>
          </li>
          <li>
            <Link to="/about" className="hover:text-gray-400">
              About
            </Link>
          </li>
          <li>
            <Link to="/services" className="hover:text-gray-400">
              Services
            </Link>
          </li>
          <li>
            <Link to="/contact" className="hover:text-gray-400">
              Contact
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default NavBar;
