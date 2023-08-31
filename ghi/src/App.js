import React, { useState } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import BarMenu from "./BarMenu";
import Nav from "./Nav";
import Homepage from "./Homepage";
import Contact from "./Contact";
import SeatGenerator from "./seats/SeatGenerator";
import MovieDetail from "./MovieDetail";
import MovieList from "./MovieList";
import MovieListAdmin from "./MovieListAdmin";
import Signup from "./Signup";
import Login from "./Login";
import "./styles/MovieDetail.css";
import BookingConfirmation from "./Booking";

function App(props) {
  const [loggedIn, setLoggedIn] = useState(false);

  return (
    <BrowserRouter>
      <Nav loggedIn={loggedIn} setLoggedIn={setLoggedIn} />
      <div className="container">
        <Routes>
          <Route path="homepage/" element={<Homepage />} />
          <Route
            path="/signup"
            element={<Signup setLoggedIn={setLoggedIn} />}
          />
          <Route path="/login" element={<Login />} />
          <Route path="seats/:showtime_id" element={<SeatGenerator />} />
          <Route path="/" element={<Navigate to="/homepage/" />} />
          <Route path="/bar" element={<BarMenu />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/movies" element={<MovieList />} />
          <Route path="/movies/admin" element={<MovieListAdmin />} />
          <Route path="/movies/:id" element={<MovieDetail />} />
          <Route path="/bookings/:user_id" element={<BookingConfirmation />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
