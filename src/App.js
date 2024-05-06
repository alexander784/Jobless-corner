import "./App.css";
import NavBar from './components/Layout/NavBar';
import {
  BrowserRouter as Router,
  Route,Routes
} from 'react-router-dom';
import Home from './pages/Home';
import Search from "./components/Layout/Search";



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
