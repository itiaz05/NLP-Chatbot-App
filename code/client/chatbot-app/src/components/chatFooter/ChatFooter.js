import React, {useState} from "react";
import "./chatFooter.css";
import SendIcon from "@mui/icons-material/Send";
import IconButton from "@mui/material/IconButton";
import apiService from "../../api";

const ChatFooter = () => {

  const [botPrediction, setBotPrediction] = useState('');
  const [msgSender, setMsgSender] = useState('');


  const onSubmit = () => {
    const resa = apiService.BotService.pred(msgSender);
    //const res = apiService.BotService.pred();
    console.log(resa);
    console.log(botPrediction);
  };

  return (
    <div className="chatFooter">
      <input className="textField" type="text" onChange={(e)=> setMsgSender(e.target.value)} />
      <IconButton className="sendButton" aria-label="send" size="large" onClick={onSubmit}>
        <SendIcon fontSize="inherit" />
      </IconButton>
    </div>
  );
};

export default ChatFooter;
