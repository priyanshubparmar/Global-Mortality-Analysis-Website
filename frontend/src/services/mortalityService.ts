// import apiClient from "../api/apiClient";

// export const getMortalityTrend = async () => {
//   const response = await apiClient.get("/mortality/test");
//   return response.data.data;
// };

import apiClient from "../api/apiClient";

export const getMortalityTrend = async () => {
  const response = await apiClient.get("/mortality/test");
  return response.data;
};