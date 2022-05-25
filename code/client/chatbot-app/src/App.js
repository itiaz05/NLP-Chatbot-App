import "./App.css";
import Fab from "@mui/material/Fab";
import ForumIcon from "@mui/icons-material/Forum";
import ChatBot from "./layout/Chatbot";
import { useState } from "react";

function App() {
  const [showChat, setShowChat] = useState(false);

  return (
    <div className="App">
      <Fab className="buttonMassanger" onClick={() => setShowChat(!showChat)}>
        <ForumIcon />
      </Fab>
      {showChat ? <ChatBot /> : null}
    </div>
  );
}

export default App;
