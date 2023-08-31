import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function BookingConfirmation() {
  const [booking, setBooking] = useState(null);
  const { user_id } = useParams();

  useEffect(() => {
    const fetchBooking = async () => {
      try {
        const bookingResponse = await fetch(
          `http://localhost:8000/bookings/user/${user_id}`
        );
        if (!bookingResponse.ok) {
          throw new Error("Failed to fetch booking data");
        }
        const bookingData = await bookingResponse.json();
        setBooking(bookingData);
      } catch (error) {
        console.error("Error fetching booking:", error);
      }
    };

    fetchBooking();
  }, [user_id]);

  if (!booking) {
    return <div>Loading...</div>;
  }

  const firstBooking = booking[0];
  const { showtime_id, reserved_seat_id, confirmation_code } = firstBooking;

  return (
    <div className="card text-center">
      <div className="card-header">Booking Confirmation</div>
      <div className="card-body">
        <h5 className="card-title">Ticket</h5>
        <p className="card-text">Show Time ID: {showtime_id}</p>
        <p className="card-text">Seat ID: {reserved_seat_id}</p>
        <p className="card-text">Confirmation Code: {confirmation_code}</p>
      </div>
    </div>
  );
}

export default BookingConfirmation;
