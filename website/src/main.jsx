

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import ZDOM from "./page/ZDOM"
import ZTOL from "./page/ZTOL"
import ZDSC from "./page/ZDSC"
import './App.css';

function App() {
  return (
    <>
    <Router>
      <Routes>
        <Route path="/" element={<ZDOM />} />
        <Route path="/ZTRD" element={<ZTOL/>} />
        <Route path="/zdsc" element={<ZDSC/>} />
      </Routes>
    </Router>
    </>
  )
}

export default App;
  
 
