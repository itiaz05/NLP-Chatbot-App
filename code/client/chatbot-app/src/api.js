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
  static pred(userInput) {
    const params = { data: String(userInput) };
    //params.append('data', String(userInput));
    return $axios
      .post('/predict/', params)
      .then((response) => {
        console.log("bot: ", response);
        return response.data.json;
      })
      .catch((error) => {
        console.log("the following error raised: ", error);
      });
  }
  static predicts(userInput) {
    const res = $axios({
      method: "post",
      url: `/predict/`,
      data: userInput,
    });
    console.log(userInput);
    console.log(String({ userInput }));
    console.log(res);
    return res;
  }


}

const apiService = { BotService };
export default apiService;
