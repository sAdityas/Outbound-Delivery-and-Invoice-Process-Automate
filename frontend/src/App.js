

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import ZDOM from "../src/page/ZDOM"
import ZTOL from "../src/page/ZTOL"
import './App.css';

function App() {
  return (
    <>
    <Router>
      <Routes>
        <Route path="/" element={<ZDOM />} />
        <Route path="/ZTRD" element={<ZTOL/>} />
      </Routes>
    </Router>
    </>
  )
}

export default App;
  
 
