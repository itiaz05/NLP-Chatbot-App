import React from "react";
import "./sender.css";

const Sender = ({ msg }) => {
  return (
    <div className="senderBox">
      <div className="senderContent">{msg}</div>
      <div>
        <div className="senderTime">{new Date().toLocaleTimeString()}</div>
      </div>
    </div>
  );
};

export default Sender;
