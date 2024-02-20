import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SignIn from "./components/SignIn";
//import Home from "./pages/Home";
import SignUp from "./components/SignUp";
import Navbar from "./components/Navbar";

function App() {
  return (
    <BrowserRouter>
    <Navbar />
    <Routes>
      <Route path="/" element={<SignIn />}/>
      <Route path="/login" element={<SignIn />}/>
      <Route path="/register" element={<SignUp />}/>
    </Routes>
    </BrowserRouter>
  );
}

export default App;
