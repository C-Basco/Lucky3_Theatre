import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";

const MovieDetail = () => {
  const { id } = useParams();
  const [movie, setMovie] = useState(null);
  const [showtimes, setShowtimes] = useState([]);

  useEffect(() => {
    const fetchMovie = async () => {
      try {
        const response = await fetch(`http://localhost:8000/movies/${id}`);
        const data = await response.json();
        setMovie(data);
      } catch (error) {
        console.error("Error fetching movie:", error);
      }
    };

    const fetchShowtimes = async () => {
      try {
        const response = await fetch(
          `http://localhost:8000/movies/${id}/showtimes`
        );
        const data = await response.json();
        setShowtimes(data);
      } catch (error) {
        console.error("Error fetching showtimes:", error);
      }
    };

    fetchMovie();
    fetchShowtimes();
  }, [id]);

  if (!movie) {
    return <div>Loading...</div>;
  }

  const handleWatchTrailer = () => {
    let trailerData;
    try {
      trailerData = JSON.parse(movie.trailer);
    } catch (error) {
      console.error("Error parsing trailer data:", error);
      console.log("Trailer data:", movie.trailer);
      return;
    }

    if (trailerData && trailerData.key) {
      const trailerKey = trailerData.key;
      const trailerUrl = `https://www.youtube.com/watch?v=${trailerKey}`;
      window.open(trailerUrl, "_blank");
    } else {
      console.error("Invalid trailer data");
      console.log("Trailer data:", trailerData);
    }
  };

  const handleTimeSlotButtonClick = (showtime_id) => {
    console.log(showtime_id);
    const url = `/seats/${showtime_id}`;

    window.location.href = url;
  };

  return (
    <div className="container-detail">
      <div className="card floating-card">
        <img src={movie.image} className="card-img" alt={movie.title} />
        <div className="card-body">
          <h5 className="card-title">{movie.title}</h5>
          <p className="card-text">{movie.description}</p>
          <div className="buttons-container">
            {showtimes.map((showtime) => (
              <button
                key={showtime.id}
                className="btn btn-danger"
                onClick={() => handleTimeSlotButtonClick(showtime.id)}
              >
                {showtime.time_slot}
              </button>
            ))}

            <button className="btn btn-danger" onClick={handleWatchTrailer}>
              Watch Trailer
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MovieDetail;
