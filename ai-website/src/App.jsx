import React from "react";
import {Route, Routes, useNavigate} from "react-router-dom";
// import './App.css';

import Dashboard from "./Pages/dashboard";

const App = () => (
  <>
    <Routes>
      <Route path="/" element={<Dashboard />} />
    </Routes>
  </>
);

export default App
