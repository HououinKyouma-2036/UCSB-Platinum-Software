import './Styles/App.css';
import './Styles/index.css';
import Navbar from './Components/Navbar';
import About from './Pages/About';
import Search from './Pages/Search';
import Clients from './Pages/Clients';
import CourseCart from './Pages/CourseCart';
import Home from './Pages/Home';
import Loading from './Pages/Loading'; 
import { Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <>
        <Navbar />
        <div>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/search" element={<Search />} />
            <Route path="/about" element={<About />} />
            <Route path="/clients" element={<Clients />} />
            <Route path="/coursecart" element={<CourseCart />} />
            <Route path="/loading" element={<Loading />} /> 
          </Routes>
        </div>
      </>
    </div>
  );
}

export default App;
