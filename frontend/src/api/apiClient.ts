// import axios from "axios";

// const apiClient = axios.create({
//   baseURL: "http://127.0.0.1:8000",
// });

// export default apiClient;


import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://localhost:8000",  // ✅ FIX
  headers: {
    "Content-Type": "application/json",
  },
});
export default apiClient;