import React from "react";
import "./chatFooter.css";
import TextField from "@mui/material/TextField";
import SendIcon from "@mui/icons-material/Send";
import IconButton from "@mui/material/IconButton";

const ChatFooter = () => {
  return (
    <div className="chatFooter">
      <input className="textField" type="text" />
      <IconButton className="sendButton" aria-label="send" size="large">
        <SendIcon fontSize="inherit" />
      </IconButton>
    </div>
  );
};

export default ChatFooter;
