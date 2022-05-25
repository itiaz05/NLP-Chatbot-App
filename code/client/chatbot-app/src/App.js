import "./App.css";
import TextareaAutosize from "@mui/material/TextareaAutosize";
import Fab from "@mui/material/Fab";
import PersonOutlineIcon from "@mui/icons-material/PersonOutline";



function App() {
  return (
    <div className="App">
      <h1>Hello! I'm Your Amdocs Bot</h1>
      <TextareaAutosize
        aria-label="messages textarea"
        placeholder="Hi!"
        style={{ width: 200 }}
      />

      <Fab
        className="chatIcon"
        size="small"
        color="secondary"
        aria-label="chatbot"
      >
        <PersonOutlineIcon />
      </Fab>
    </div>
  );
}

export default App;
