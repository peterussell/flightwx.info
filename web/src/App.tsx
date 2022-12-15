import { Route, Routes } from "react-router-dom";
import LandingPage from "pages/landing";
import LoginPage from "pages/login";
import { NavBar } from "features/navbar/components";

import "./App.css";

const App = () => {
  return (
    <div className="app-container">
      <NavBar />
      <Routes>
        <Route path="login" element={<LoginPage />} />
        <Route index element={<LandingPage />} />
      </Routes>
    </div>
  );
};
export default App;
