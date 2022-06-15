import Axios from "axios";

const APP_API_ENDPOINT = "http://localhost:5000/api";

const $axios = Axios.create({
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
    "Access-Control-Allow-Origin": "*",
  },
});
$axios.defaults.baseURL = APP_API_ENDPOINT;

class BotService {
  static pred(userInput) {
    const params = { data: String(userInput) };
    //params.append('data', String(userInput));
    return $axios
      .post("/predict/", params)
      .then((response) => {
        return response.data;
      })
      .catch((error) => {
        console.log("the following error raised: ", error);
      });
  }
}

const apiService = { BotService };
export default apiService;
