DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS reserved_seats;
DROP TABLE IF EXISTS showtimes;
DROP TABLE IF EXISTS bookings;


CREATE TABLE IF NOT EXISTS users (
    id SERIAL NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    hashed_password TEXT NOT NULL UNIQUE,
    first TEXT NOT NULL,
    last TEXT NOT NULL
    );

CREATE TABLE IF NOT EXISTS movies (
    id SERIAL NOT NULL UNIQUE,
    title TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    image TEXT NOT NULL UNIQUE,
    trailer JSON
    );

CREATE TABLE IF NOT EXISTS upcoming_movies (
    id SERIAL NOT NULL UNIQUE,
    title TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    image TEXT NOT NULL UNIQUE,
    trailer JSON NOT NULL
    );

CREATE TABLE IF NOT EXISTS rooms (
    id SERIAL NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS showtimes (
    id SERIAL NOT NULL UNIQUE,
    room_id INT NOT NULL REFERENCES rooms(id),
    movie_id INT NOT NULL REFERENCES movies(id),
    time_slot TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS reserved_seats (
    id SERIAL NOT NULL UNIQUE,
    showtime_id INT NOT NULL REFERENCES showtimes(id),
    user_id INT NOT NULL REFERENCES users(id),
    available BOOLEAN NOT NULL,
    seat_id TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS bookings (
    id SERIAL PRIMARY KEY,
    showtime_id INTEGER NOT NULL REFERENCES showtimes(id),
    reserved_seat_id INTEGER NOT NULL REFERENCES reserved_seats(id),
    user_id INTEGER NOT NULL REFERENCES users(id),
    confirmation_code TEXT
);
