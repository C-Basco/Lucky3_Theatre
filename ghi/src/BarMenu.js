import React from "react";

import pic1 from "./picture/1.png";
import pic2 from "./picture/2.png";
import pic3 from "./picture/3.png";
import pic4 from "./picture/4.png";

const BarMenu = () => {
  const pictures = [pic1, pic2, pic3, pic4];

  return (
    <div style={{ marginTop: "100px" }}>
      <div
        className="bar-div"
        style={{
          columnCount: 2,
          columnGap: "20px",
          rowGap: "20px",
          transform: "scale(1.2)",
        }}
      >
        {pictures.map((picture, index) => (
          <div key={index} className="card p-0 border-0">
            <img
              className="card-img-top"
              src={picture}
              alt={`Image ${index + 1}`}
            />
          </div>
        ))}
      </div>
    </div>
  );
};

export default BarMenu;
