// const Navbar = () => {
//   return (
//     <div
//       style={{
//         height: "60px",
//         background: "#1e293b",
//         color: "white",
//         display: "flex",
//         alignItems: "center",
//         paddingLeft: "20px",
//         fontWeight: "bold",
//         fontSize: "18px",
//       }}
//     >
//       Global Mortality Analytics
//     </div>
//   );
// };

// export default Navbar;

// const Navbar = () => {
//   return (
//     <header className="navbar">
//       <h2>Global Mortality Analytics</h2>
//     </header>
//   );
// };

// export default Navbar;

import logo from "../assets/logo.png";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <header className="navbar">

      <div className="nav-left">
        <Link to="/" className="logo">
          <img src={logo} alt="Mortality Analytics Logo" />
        </Link>
      </div>

      <nav className="nav-center">

        <Link to="/">Home</Link>

        <Link to="/country">Country Explorer</Link>

        <Link to="/comparison">Compare Countries</Link>

        <Link to="/life-table">Life Table</Link>

        <Link to="/causes">Causes of Death</Link>

        <Link to="/about">About</Link>

      </nav>

      <div className="nav-right">

        <Link to="/dashboard" className="dashboard-btn">
          Dashboard
        </Link>

      </div>


    </header>
  );
};

export default Navbar;