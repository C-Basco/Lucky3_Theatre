import React, { useEffect, useState } from "react";
import { Legend } from "./components/legend";
import { TableHeader } from "./components/tableHeader";
import { generate_confirmation_code } from "./components/confirmationCode";
import { useParams } from "react-router-dom";
import "../styles/seat.css";

function SeatBooking(props) {
  const { showtime_id } = useParams();

  const [reserved_seat_id, setReservedSeatId] = useState([]);

  const [reserved, setReserved] = useState([]);
  const [selectedSeatId, setSelectedSeatId] = useState([]);
  const [user_id, setUser_id] = useState(null);

  const fetchUserId = async () => {
    try {
      const userResponse = await fetch("http://localhost:8000/accounts/user");
      if (!userResponse.ok) {
        throw new Error("Failed to fetch user_id");
      }
      const userData = await userResponse.json();
      setUser_id(userData.user_id);
    } catch (error) {
      console.error("Error getting user_id:", error);
    }
  };

  const fetchData = async () => {
    try {
      const url = "http://localhost:8000/seats";
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      const seatUpdate = data.map((currentSeat) => {
        currentSeat.disabled = !currentSeat.available;
        return currentSeat;
      });
      setReserved(seatUpdate);
      setReservedSeatId(data[0].id);
    } catch (error) {
      console.error("Error getting seat data:", error);
    }
  };

  useEffect(() => {
    fetchUserId();
    fetchData();
  }, []);

  const handleOnClick = async (event) => {
    event.preventDefault();
    const data = {};
    data.showtime_id = showtime_id;
    data.user_id = 1;
    data.seat_id = selectedSeatId;

    const confirmation_code = generate_confirmation_code();
    data.confirmation_code = confirmation_code;

    const seatUrl = "http://localhost:8000/res_seats";
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch(seatUrl, fetchConfig);
    if (response.ok) {
      const res_seat_data = await response.json();
      console.log("This is the data:", res_seat_data);
      setReserved([res_seat_data, ...reserved]);
    }

    const bookingData = {
      showtime_id: parseInt(showtime_id),
      reserved_seat_id: Array.isArray(reserved_seat_id)
        ? reserved_seat_id.map((seatIds) => parseInt(seatIds))
        : [parseInt(reserved_seat_id)],
      user_id: 1, //Replace with code when login finished
      confirmation_code: confirmation_code,
    };
    const bookingResponse = await fetch("http://localhost:8000/bookings", {
      method: "post",
      body: JSON.stringify(bookingData),
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (bookingResponse.ok) {
      const bookingData = await bookingResponse.json();
    }
  };

  const choiceSeat = (seat_id) => {
    setSelectedSeatId([seat_id, ...selectedSeatId]);
    const newReservedSeats = reserved.map((currentSeat) => {
      if (currentSeat.seat_id === seat_id) {
        return { ...currentSeat, available: !currentSeat.available };
      }
      return currentSeat;
    });
    setReserved(newReservedSeats);
  };

  const getSeatObject = (seat_id) => {
    if (reserved?.length > 0) {
      return reserved.filter((thisSeat) => thisSeat.seat_id === seat_id)[0];
    }
  };

  const seatsColumns = ["1", "2", "3","4", "5", "", "6", "7","8", "9","10","11","12",];
  const seatsRows = ["A", "B", "C", "D", "E", "", "F", "G", "H", "I", "J"];
  const seatsGenerator = () => {
    return (
      <table id="seatsBlock">
        <tbody>
          <TableHeader seatsColumns={seatsColumns} />
          {seatsRows.map((row, index) =>
            row === "" ? (
              <tr key={index} className="seatVGap" />
            ) : (
              <tr key={index}>
                <td>{row}</td>
                {seatsColumns.map((column, index) => {
                  return column === "" ? (
                    <td key={index} className="seatGap" />
                  ) : (
                    <td key={index}>
                      <input
                        onClick={() => choiceSeat(`${row}${column}`)}
                        type="checkbox"
                        className="seats"
                        id={`${row}${column}`}
                        value={`${row}${column}`}
                        disabled={
                          getSeatObject(`${row}${column}`)
                            ? getSeatObject(`${row}${column}`).disabled
                            : false
                        }
                      />
                    </td>
                  );
                })}
              </tr>
            )
          )}
        </tbody>
      </table>
    );
  };
  return (
    <div>
      <h1>Movie Seat Selection</h1>
      <div className="container">
        <div className="screen">
          <h2 className="wthree">Screen this way</h2>
        </div>
        <div className="w3ls-reg" style={{ paddingTop: "0px" }}>
          <div
            className="seatStructure txt-center"
            style={{ overflowX: "auto" }}
          >
            {seatsGenerator()}
            <Legend />
            <button onClick={handleOnClick}>Book Seats</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default SeatBooking;
