import apiClient from "../api/apiClient";

export const getFilters = async () => {
  const response = await apiClient.get("/filters");
  return response.data;
};

export const getLifeTableAnalysis = async (
  location: string,
  gender: string,
  year: number,
  age: number
) => {
  const response = await apiClient.get("/life-table/analysis", {
    params: {
      location,
      gender,
      year,
      age,
    },
  });

  return response.data;
};

