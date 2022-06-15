import React from "react";
import "./reciver.css";

const Reciver = ({ msg }) => {
  return (
    <div className="reciverBox">
      <div className="reciverContent">{msg}</div>
      <div>
        <div className="reciverTime">{new Date().toLocaleTimeString()}</div>
      </div>
    </div>
  );
};

export default Reciver;
