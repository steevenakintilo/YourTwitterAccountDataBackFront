import logo from './logo.svg';
import './App.css';
import StartPage from './pages/StartPage';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<StartPage />} />
          <Route path="/DisplayData" element={<StartPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
