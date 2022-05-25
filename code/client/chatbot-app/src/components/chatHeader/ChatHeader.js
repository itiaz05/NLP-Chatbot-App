import React from "react";
import "./chatHeader.css";
import Avatar from "@mui/material/Avatar";
import Typography from "@mui/material/Typography";

const ChatHeader = () => {
  return (
    <div className="chatHeader">
      <Avatar
        alt="AmdocsAvatarImg"
        src="https://www.meda-conferences.com/wp-content/uploads/2019/02/amdocs-2017-stacked-brand-mark-rgb-250x248.png"
      />
      <Typography>Amdocs</Typography>
    </div>
  );
};

export default ChatHeader;
