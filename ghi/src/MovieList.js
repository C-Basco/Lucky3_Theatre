import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const MovieList = () => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchMovies = async () => {
      try {
        const response = await fetch("http://localhost:8000/movies");
        const data = await response.json();
        setMovies(data);
      } catch (error) {
        console.error("Error fetching movies:", error);
      }
    };

    fetchMovies();
  }, []);

  return (
    <div className="container">
      <h2>Movie List</h2>
      <div className="row">
        {movies.map((movie) => (
          <div className="col-md-4 mb-4" key={movie.id}>
            <div className="card">
              <img
                src={movie.image}
                className="card-img-top"
                alt={movie.title}
              />
              <div className="card-body">
                <h5 className="card-title">
                  <Link
                    to={`/movies/${movie.id}`}
                    style={{ textDecoration: "none", color: "black" }}
                  >
                    {movie.title}
                  </Link>
                </h5>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MovieList;
