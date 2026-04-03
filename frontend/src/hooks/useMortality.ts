// import { useEffect, useState } from "react";
// import { getMortalityTrend } from "../services/mortalityService";

// export const useMortality = () => {
//   const [data, setData] = useState([]);
//   const [loading, setLoading] = useState(true);

//   useEffect(() => {
//     const fetchData = async () => {
//       try {
//         const result = await getMortalityTrend();
//         setData(result);
//       } catch (error) {
//         console.error("Error loading mortality data", error);
//       } finally {
//         setLoading(false);
//       }
//     };

//     fetchData();
//   }, []);

//   return { data, loading };
// };