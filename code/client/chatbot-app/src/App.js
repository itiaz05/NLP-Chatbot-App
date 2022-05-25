import "./App.css";
import Fab from "@mui/material/Fab";
import ForumIcon from "@mui/icons-material/Forum";
import ChatHeader from "./components/chatHeader/ChatHeader";
import TextField from "@mui/material/TextField";
import ChatFooter from "./components/chatFooter/ChatFooter";

function App() {
  return (
    <div className="App">
      <div className="chatbox">
        <div className="chatHeader">
          <ChatHeader />
        </div>
        <div></div>
        <div className="chatFooter">
          <ChatFooter />
        </div>
      </div>
      <Fab className="buttonMassanger">
        <ForumIcon />
      </Fab>
    </div>
  );
}

export default App;
