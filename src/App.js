import "./App.css";
import NavBar from './components/Layout/NavBar';
import {
  BrowserRouter as Router,
  Route,Routes
} from 'react-router-dom';
import Home from './pages/Home';
import Search from "./components/Layout/Search";
import Login from "./components/Layout/Login";
import PostRole from "./pages/PostRole";



function App() {
  return (
    <>
    <Router>
    <NavBar />

    <Routes>
      <Route path='/' element={ <Home />} />
      <Route path='/Login' element={ <Login />} />
      <Route path='/PostRole' element={ <PostRole />} />



      
    </Routes>
    </Router>


  

    
    </>
  );
}

export default App;
