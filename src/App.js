import "./App.css";
import NavBar from './components/Layout/NavBar';
import Nav from 'react-bootstrap/Nav';
import 'bootstrap/dist/css/bootstrap.min.css';
import {
  BrowserRouter as Router,
  Route,Routes
} from 'react-router-dom';
import Home from './pages/Home';



function App() {
  return (
    <>
    <Router>

    <NavBar />
    <Routes>
      <Route path='/' element={ <Home />} />

      
    </Routes>
    </Router>

  

    
    </>
  );
}

export default App;
