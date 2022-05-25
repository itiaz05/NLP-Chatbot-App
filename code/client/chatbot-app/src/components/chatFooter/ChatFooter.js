import React, {useState} from "react";
import "./chatFooter.css";
import SendIcon from "@mui/icons-material/Send";
import IconButton from "@mui/material/IconButton";
import apiService from "../../api";

const ChatFooter = () => {

  const [botPrediction, setBotPrediction] = useState('');
    const [value, setValue] = useState("");


  const onSubmit = (userInput) => {
    apiService.BotService.predictUserInput(userInput).then(response => {
      setBotPrediction(response);
    });
  };

  return (
    <div className="chatFooter">
      <input className="textField" type="text" value={setValue(this.value)}/>
      <IconButton className="sendButton" aria-label="send" size="large" onClick={onSubmit(value)}>
        <SendIcon fontSize="inherit" />
      </IconButton>
    </div>
  );
};

export default ChatFooter;
