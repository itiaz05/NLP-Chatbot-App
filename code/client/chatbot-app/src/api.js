import Axios from "axios";

const $axios = Axios.create({
  baseURL: "/api/",
  headers: { "Content-Type": "application/json" },
});

const getOnBeforeRequestHandler = () => (config) => config;

const onRequestErrorHandler = () => (error) => Promise.reject(error);

const getOnResponseHandler = () => (response) => response;

const onResponseErrorHandler = () => (error) => {
  throw error;
};

$axios.interceptors.request.use(
  getOnBeforeRequestHandler(),
  onRequestErrorHandler()
);
$axios.interceptors.response.use(
  getOnResponseHandler(),
  onResponseErrorHandler()
);

class ChatBox {
  constructor() {
    this.args = {
      openButton: document.querySelector(".chatbox_button"),
      chatBox: document.querySelector(".chatbox_support"),
      sendButton: document.querySelector(".send_button"),
    };
    this.state = false;
    this.messages = [];
  }
}

class BotService {
  static predictUserInput(userInput) {
    return $axios
      .get("api/predict/${userInput}/", { userInput })
      .then((response) => response.data);
  }
}

const apiService = { ChatBox, BotService };
export default apiService;
