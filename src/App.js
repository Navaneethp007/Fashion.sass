import logo from './logo.svg';
import './App.css';
import { Container, Row, Col } from 'react-bootstrap';
import Home from './pages/home/home';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Home />} />

    </Routes>
    </BrowserRouter>
  );
}

export default App;
