import Axios from "axios";

const APP_API_ENDPOINT = "http://localhost:5000/api";

const $axios = Axios.create({
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
    "Access-Control-Allow-Origin": "*",
    Origin: "http://localhost:3000",
  },
});
$axios.defaults.baseURL = APP_API_ENDPOINT;

const getOnBeforeRequestHandler = () => (config) => config;

class BotService {
  static async predictUserInput() {
    const response = await $axios.get(`http://localhost:5000/api/predicts/`);
    return response;
  }

  static pred(userInput) {
    return $axios
      .get(`/predict/`, {
        data: userInput,
        //header: axious_allow_header,
      })
      .then((response) => {
        console.log("bot: ", response);
        return response.data.json;
      }).catch((error) => {
        console.log("the following error raised: ", error);
      });
  }
  static predixc(userInput) {
    const res = $axios({
      method: "post",
      url: `/predict/${userInput}`,
      data: userInput,
    });
    console.log(userInput);
    console.log(String({ userInput }));
    console.log(res);
    return res;
  }

  static predict1 = (userInput) => (async) => {
    try {
      const res = $axios.get(`/predict/${userInput}`, userInput);
      return res;
    } catch (err) {
      console.log(err.to_dict());
    }
    return "ok";
  };
}

const apiService = { BotService };
export default apiService;
