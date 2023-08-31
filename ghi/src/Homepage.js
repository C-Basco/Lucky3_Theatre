import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
//import { Link } from "react-router-dom";

function Homepage() {
  const [upcomingMovies, setUpcomingMovies] = useState([]);
  const [movies, setMovies] = useState([]);
  const [activeSlide, setActiveSlide] = useState(0);

  const fetchUpcomingMovies = async () => {
    try {
      const url = "http://localhost:8000/upcoming_movies";
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setUpcomingMovies(data);
      } else {
        console.error("Error fetching movies:", response.statusText);
      }
    } catch (error) {
      console.error("Error fetching movies:", error);
    }
  };

  const fetchMovies = async () => {
    try {
      const url = "http://localhost:8000/movies";
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setMovies(data);
      } else {
        console.error("Error fetching movies:", response.statusText);
      }
    } catch (error) {
      console.error("Error fetching movies:", error);
    }
  };

  useEffect(() => {
    fetchUpcomingMovies();
    fetchMovies();
  }, []);

  if (!upcomingMovies) {
    return null;
  }

  const handleSlideChange = (selectedIndex) => {
    setActiveSlide(selectedIndex);
  };

  return (
    <div className="Homepage section">
      <h1>is it working?</h1>
      <div className="Upcoming">
        <div className="row">
          <div
            id="carouselExampleIndicators"
            class="carousel slide"
            data-ride="carousel"
          >
            <div className="carousel-indicators">
              {upcomingMovies.slice(0, 3).map((_, index) => (
                <>
                  <button
                    type="button"
                    key={index}
                    data-mdb-target="#carouselExampleIndicators"
                    data-mdb-slide-to={index}
                    className={index === activeSlide ? "active" : ""}
                  ></button>
                </>
              ))}
            </div>
            <div class="carousel-inner">
              {upcomingMovies.slice(0, 3).map((upmovie, index) => (
                <>
                  <div
                    key={index}
                    className={`carousel-item ${
                      index === activeSlide ? "active" : ""
                    }`}
                  >
                    <img
                      className="d-block w-100"
                      src={upmovie.image}
                      alt={`Slide ${index + 1}`}
                    />
                  </div>
                </>
              ))}
            </div>
            <a
              className="carousel-control-prev"
              href="#carouselExampleIndicators"
              role="button"
              data-slide="prev"
              onClick={() =>
                handleSlideChange(
                  (activeSlide - 1 + upcomingMovies.length) %
                    upcomingMovies.length
                )
              }
            >
              <span
                className="carousel-control-prev-icon"
                aria-hidden="true"
              ></span>
              <span class="sr-only">Previous</span>
            </a>
            <a
              className="carousel-control-next"
              href="#carouselExampleIndicators"
              role="button"
              data-slide="next"
              onClick={() =>
                handleSlideChange(
                  (activeSlide + 1 + upcomingMovies.length) %
                    upcomingMovies.length
                )
              }
            >
              <span
                className="carousel-control-next-icon"
                aria-hidden="true"
              ></span>
              <span class="sr-only">Next</span>
            </a>
          </div>
        </div>
      </div>
      <div className="Now playing">
        <div className="row">
          {movies.slice(0, 4).map((movie) => (
            <>
              <div className="col-md-4 mb-4" key={movie.id}>
                <div className="card">
                  <img
                    className="card-img-top"
                    src={movie.image}
                    alt="Card image cap"
                  />
                  <div className="card-body ">
                    <h5 className="card-title">
                      <Link
                        to={`/movies/${movie.id}`}
                        style={{ textDecoration: "none", color: "black" }}
                      >
                        {movie.title}
                      </Link>
                    </h5>
                    <p className="card-text ">{movie.description}</p>
                  </div>
                  <div className="card-body">
                    <a href="#" className="card-link">
                      Card link
                    </a>
                  </div>
                </div>
              </div>
            </>
          ))}
        </div>
      </div>
      <div className="Snacks"></div>
    </div>
  );
}

export default Homepage;
