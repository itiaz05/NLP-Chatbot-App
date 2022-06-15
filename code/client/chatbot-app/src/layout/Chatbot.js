import "./chatbot.css";
import React from "react";
import { Paper } from "@mui/material";
import Sender from "../components/massageTemplate/sender/Sender";
import Reciver from "../components/massageTemplate/reciver/Reciver";
import SendIcon from "@mui/icons-material/Send";
import Avatar from "@mui/material/Avatar";
import Typography from "@mui/material/Typography";
import { useState, useEffect, useRef } from "react";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import apiService from "./../api";

const ChatBot = () => {
  const welcomeMsg = "Welcome, how can i help you? (for exit type quit)";
  const [msg, setMsg] = useState("");
  const lastMassageRef = useRef(null);
  const [history, setHistory] = useState([
    {
      component: <Reciver msg={welcomeMsg} />,
    },
  ]);

  function handleClick(userMsg) {
    document.getElementById("msgField").value = ""; // Clear input text after submit
    if (userMsg === "") {
      return;
    } else {
      apiService.BotService.pred(userMsg).then((response) => {
        const newHistory = history.map((msg) => msg); // Create new history array to cause React re-render
        newHistory.push(
          { component: <Sender msg={userMsg} /> },
          { component: <Reciver msg={response} /> }
        );
        setHistory(newHistory);
      });
    }
  }

  useEffect(() => {
    lastMassageRef.current.scrollIntoView();
    setMsg("");
  }, [history]);

  return (
    <div className="chatbox">
      <Paper>
        <div className="chatHeader">
          <Avatar
            className="avatar"
            alt="AmdocsAvatarImg"
            src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALQAAAC0CAMAAAAKE/YAAAABR1BMVEUAAADgFYLlOmjlOGrlNmvkNGzkMW/kL3DjLXHjK3PjKHXiJnbiJHjznCPznSLlPGfhH3zymCbmP2XmQmLzoSDylCnnRmDxkCvxjC7wiDHwhTPvgTbvfjjuezrueDztdT/tcULsbEXrZ0jrYkzqXk/qWlLpVVXoUFnnS1yoEmD0phz1qxmsLU49JwkPCgI9KwZ6TxF5SRUcAxB+DElNNgd7VwxbPAzklR8OAgg8IQ07HRA6FBaIVhV4QRt3Ox92NCR1KyofFAQuHgY7GROtM0lwDEC1ayG0ZCazXSuyVzCxUDWwSDqvQT+uOURUCDHSFHqaDlmZaRHWlhWKYQ24ghHUhSGCKDU4Bx8qBxZ0KSzJOlaQKD5WGCZrSA1yGzW5KFqOG0fGHWs5Dxq2cR2odRFaNhCmaBtzHjOXWxpLLQ4rDhLGhxZIFR5EfIrNAAADpklEQVR4nO2caVdTMRCGWxUVZUfZ950ulxbKBaUutyLuC7IoLTuFAuX/f7aLWjjkWpJMJuWc9/kBOc/JyZ0kk5kbCAAAAAAAAAAAAAAAAAAAAAAAgCyxCvEKL/7xssyrCq/LbJVYOrQhnX1SoKmpsbG1tfVpgc7Orq6u7u7unp7e3t6+vv7+gYHBwaGhoeHh4ZGRkdHR0bGxsfHxiYmJycnJqampjo6OdGZ7kVl6R1u6va2tObLNKu2RSDffubvLOd0LRNL36nb5pJNk0nV7v7ikE3TS9x+wTTal9MN9ppWdpZSu3+Oxdkmlmaw9WulHPNZ5WunH3zmkk8TSDW8ZpKPU0g0/GawXqKUPGJb1CbU0xwJxyaVbZo1Le/TSc8alA3lyaYapjtFLm5/qFL30N+PSgeglnl3meYU3FZb+srXsJ93y1by1MofLPtIMn6IGm2LpA9te/ycnlA6ajx9aZITSHAcQDWaF0hxnPR0yIuna/hILIUQkPW3bqhq3Ujp9G6UjkGYC0lxAmgtIcwFpSVJn8fhKgXdl3pf4UORjmU8lPpf4UmS5SCRS5ewxN30NmsSZt3NEeRu/Ij0dvAbFvdfdIE4hVJPWTmI7sQXyvEc1ad28iEue6r2BdFDrzdGjfd26sbTObSxB98wsJ60REddCVA/6stLqeZHVkD1p1aBXcLYnrRj0is72pNWC3nzIqrRS3mwmbFlaIeg5IdvSCkEvG7YtLR/0ZsL2paXzqj9qQFo26LnhGpAOKky0fWm5TbG4omtAWi7ordaGtNymGPKTXjn2pAb6A8dtPBEWSx9FFQfkkF4TS586qgNySK8LpU/UB+SQDoukN5TnmUXaE0ofa4zIID0jkt7QGZFBOiGSTuqMyCA9L5I+0xnRlrRqiC4BaTH0y4PhbZz8QzxnkCYPeTmGeo+UcHNRX9SLaY7KGuJtPCc8T1MX5okPTKeKox2KLwHUnTp+R1M153ahNHndpu8lQP7aspjzuW7RtzP4XrdOz6RW9vkmY60pw8WWvi3AfArBRFWe8WSNiaJN02kxM6/5hhOQZqpjE0alTbVvrZuUNlU77Rl8vjDXD5AwJm2yt2/NkLTZdjNDj59mG7GdvAHpetPN406WXpqh4X2VWJqnSd8llebqdU/l6aQZf+EQIyq82mftISIpcYuw/wjG2dEsJsyw/SXjCqmkatlmOnNhxbiME3XjJ3IFspu5ixrvhgMAAAAAAAAAAAAAAAAAAAC3ht8ESdIdA+XZzQAAAABJRU5ErkJggg=="
          />
          <Typography className="headerSubText">Amdocs</Typography>
        </div>
      </Paper>
      <Paper className="chatContent">
        {history.map((obj, index) => {
          return (
            <div className="msg" key={index}>
              {obj.component}
            </div>
          );
        })}
        <div ref={lastMassageRef} />
      </Paper>
      <Paper>
        <TextField
          id="msgField"
          autoComplete="off"
          placeholder="Text something..."
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              handleClick(msg);
            }
          }}
          onChange={(e) => setMsg(e.target.value)}
          className="textField"
          type="text"
        />
        <Button
          variant="contained"
          className="sendButton"
          onClick={() => {
            handleClick(msg);
          }}
          aria-label="send_msg"
          sx={{ height: "9.7vh" }}
        >
          <SendIcon />
        </Button>
      </Paper>
    </div>
  );
};

export default ChatBot;
