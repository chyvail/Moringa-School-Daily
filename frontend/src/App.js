import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SignIn from "./components/SignIn";
import Home from "./pages/Home";
import SignUp from "./components/SignUp";

function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Home />}/>
      <Route path="/login" element={<SignIn />}/>
      <Route path="/register" element={<SignUp />}/>
    </Routes>
    </BrowserRouter>
  );
}

export default App;
