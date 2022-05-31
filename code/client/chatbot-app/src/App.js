import "./App.css";
import Fab from "@mui/material/Fab";
import ForumIcon from "@mui/icons-material/Forum";
import ChatBot from "./layout/Chatbot";
import { useState } from "react";
import Grid from "@mui/material/Grid";

function App() {
  const [showChat, setShowChat] = useState(false);

  return (
    <div className="App">
      {showChat ? (
        <div>
          <Grid container>
            <Grid item xs={12} sm={6} md={5}>
              <ChatBot />
            </Grid>
          </Grid>
        </div>
      ) : null}
      <Fab className="buttonMassanger" onClick={() => setShowChat(!showChat)}>
        <ForumIcon />
      </Fab>
    </div>
  );
}

export default App;
