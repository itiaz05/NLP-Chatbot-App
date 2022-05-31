import React from "react";
import "./chatbot.css";
import ChatHeader from "../components/chatHeader/ChatHeader";
import ChatFooter from "../components/chatFooter/ChatFooter";
import { Paper } from "@mui/material";

const ChatBot = () => {
  return (
    <div>
      <Paper>
        <ChatHeader />
      </Paper>
      <Paper className="chatContent">Main Content</Paper>
      <Paper>
        <ChatFooter />
      </Paper>
    </div>
  );
};

export default ChatBot;
