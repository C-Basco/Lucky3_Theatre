import React from "react";
import { NavLink, useNavigate } from "react-router-dom";
import logoIcon from "./picture/Popcorn.png";

function Nav({ loggedIn, setLoggedIn }) {
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      const response = await fetch(
        "http://localhost:8000/api/accounts/logout",
        {
          method: "POST",
          credentials: "include",
        }
      );

      if (!response.ok) {
        throw new Error("Failed to logout");
      }

      setLoggedIn(false);
      navigate("/login");
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-red">
      <div className="container">
        <NavLink className="navbar-brand" to="/homepage">
          <img src={logoIcon} alt="Logo" className="brand-logo" />
        </NavLink>
        <div className="collapse navbar-collapse">
          <ul className="navbar-nav ml-auto">
            <li className="nav-item">
              <NavLink className="nav-link" to="/movies">
                Movies
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/bar">
                Bar
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/contact">
                Contact
              </NavLink>
            </li>
            <li className="nav-item dropdown">
              <a
                className="nav-link dropdown-toggle"
                href="#"
                id="navbarDropdownMenuLink"
                role="button"
                data-bs-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                Account
              </a>
              <ul
                className="dropdown-menu dropdown-menu-right"
                aria-labelledby="navbarDropdownMenuLink"
              >
                {loggedIn ? (
                  <li>
                    <button
                      className="dropdown-item btn btn-link"
                      onClick={handleLogout}
                    >
                      Logout
                    </button>
                  </li>
                ) : (
                  <>
                    <li>
                      <NavLink className="dropdown-item" to="/login">
                        Login
                      </NavLink>
                    </li>
                    <li>
                      <NavLink className="dropdown-item" to="/signup">
                        Signup
                      </NavLink>
                    </li>
                    <li>
                      <NavLink className="dropdown-item" to="/movies/admin">
                        Admin
                      </NavLink>
                    </li>
                  </>
                )}
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Nav;
