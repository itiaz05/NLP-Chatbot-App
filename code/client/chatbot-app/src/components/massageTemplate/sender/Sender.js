import React from "react";
import "./sender.css";

const Sender = ({ msg, time }) => {
  return (
    <div className="senderBox">
      <div className="senderContent">{msg}</div>
      <div>
        <div className="senderTime">{time}</div>
      </div>
    </div>
  );
};

export default Sender;
