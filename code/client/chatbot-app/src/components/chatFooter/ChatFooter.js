import React from "react";
import "./chatFooter.css";
import SendIcon from "@mui/icons-material/Send";
import IconButton from "@mui/material/IconButton";

const ChatFooter = () => {
  return (
    <div>
      <input className="textField" type="text" />
      <IconButton
        className="sendButton"
        aria-label="send"
        size="large"
        sx={{ backgroundColor: "rgb(202, 217, 232)" }}
      >
        <SendIcon fontSize="inherit" />
      </IconButton>
    </div>
  );
};

export default ChatFooter;
