
// import { Link } from "react-router-dom";

// const Sidebar = () => {
//   return (
//     <div
//       style={{
//         width: "220px",
//         background: "#0f172a",
//         color: "white",
//         padding: "20px",
//       }}
//     >
//       <nav style={{ display: "flex", flexDirection: "column", gap: "15px" }}>
//         <Link to="/" style={{ color: "white", textDecoration: "none" }}>
//           Dashboard
//         </Link>

//         <Link to="/mortality" style={{ color: "white", textDecoration: "none" }}>
//           Mortality Explorer
//         </Link>

//         <Link to="/population" style={{ color: "white", textDecoration: "none" }}>
//           Population
//         </Link>

//         <Link to="/prediction" style={{ color: "white", textDecoration: "none" }}>
//           Prediction
//         </Link>
//       </nav>
//     </div>
//   );
// };

// export default Sidebar;

import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <aside className="sidebar">
      <nav>
        <Link to="/">Home</Link>
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/mortality">Mortality</Link>
        <Link to="/population">Population</Link>
        <Link to="/prediction">Prediction</Link>
        <Link to="/donation">Donation</Link>
      </nav>
    </aside>
  );
};

export default Sidebar;