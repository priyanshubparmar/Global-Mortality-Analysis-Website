// import React from "react";
// import Navbar from "./Navbar";
// import Sidebar from "./Sidebar";

// interface Props {
//   children: React.ReactNode;
// }

// const PageContainer = ({ children }: Props) => {
//   return (
//     <div className="layout">
//       <Navbar />

//       <div className="layout-body">
//         <Sidebar />

//         <main className="page-content">{children}</main>
//       </div>
//     </div>
//   );
// };

// export default PageContainer;

import type { ReactNode } from "react";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

interface Props {
  children: ReactNode;
}

const PageContainer = ({ children }: Props) => {
  return (
    <div className="layout">
      <Navbar />

      <div className="layout-body">
        <Sidebar />
        <main className="page-content">{children}</main>
      </div>
    </div>
  );
};

export default PageContainer;