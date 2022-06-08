import "./App.css";
import Fab from "@mui/material/Fab";
import ForumIcon from "@mui/icons-material/Forum";
import ChatBot from "./layout/Chatbot";
import { useState } from "react";
import Fade from "@mui/material/Fade";

function App() {
  const [showChat, setShowChat] = useState(false);

  return (
    <div className="App">
      {showChat ? (
        <div className="chat-visible">
          <ChatBot />
        </div>
      ) : null}
      <Fab className="buttonMassanger" onClick={() => setShowChat(!showChat)}>
        <ForumIcon />
      </Fab>
    </div>
  );
}

export default App;
