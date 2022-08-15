import { Route, Routes } from "react-router-dom";
import LandingPage from "pages/landing";
import LoginPage from "pages/login";
import { NavBar } from "features/navbar/components";

const App = () => {
  return (
    <>
      <NavBar />
      <Routes>
        <Route path="login" element={<LoginPage />} />
        <Route index element={<LandingPage />} />
      </Routes>
    </>
  );
};
export default App;
