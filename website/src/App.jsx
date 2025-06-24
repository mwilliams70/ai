import React from "react";
import {Route, Routes, useNavigate} from "react-router-dom";

import Dashboard from "./Pages/dashboard"

const App = () => (
    <>
        <Routes>
            <Route path="dashboard" element={<Dashboard />} />
        </Routes>
    </>
);

export default App