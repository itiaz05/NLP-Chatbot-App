import React from "react";
import "./chatbot.css";
import ChatHeader from "../components/chatHeader/ChatHeader";
import ChatFooter from "../components/chatFooter/ChatFooter";

const ChatBot = () => {
  return (
    <div className="chatbox">
      <div className="chatHeader">
        <ChatHeader />
      </div>
      <div className="chatContent">Main Content</div>
      <div className="chatFooter">
        <ChatFooter />
      </div>
    </div>
  );
};

export default ChatBot;
