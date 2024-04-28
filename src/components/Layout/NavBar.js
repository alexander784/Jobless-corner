import React from 'react'

import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { NavLink, useNavigate } from "react-router-dom";


const NavBar = () => {
  return (
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Crabs Jobs</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          {/* <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li> */}
          <li class="nav-item">
            <a class="nav-link" href="#">Jobs</a>
          </li>
          <Row className="nav-links">
          <Col>
            <NavLink  to="/students" className="nav-link">
              Login
            </NavLink>
          </Col>
          <Col>
            <NavLink to="/pairs" className="nav-link">
              SignUp
            </NavLink>
          </Col>
          </Row>
          
          {/* <li class="nav-item">
            <a class="nav-link" href="#">Pricing</a>
          </li> */}
          
        </ul>
      </div>
    </div>
  </nav>
  )
}

export default NavBar;