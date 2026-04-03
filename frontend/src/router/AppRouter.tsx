import { BrowserRouter, Routes, Route } from "react-router-dom";

import PageContainer from "../layout/PageContainer";

import DashboardPage from "../pages/dashboard/DashboardPage";
import HomePage from "../pages/home/HomePage";
import MortalityPage from "../pages/mortality/MortalityPage";
import PopulationPage from "../pages/population/PopulationPage";
import PredictionPage from "../pages/prediction/PredictionPage";
import DonationPage from "../pages/donation/DonationPage";
import LifeTablePage from "../pages/LifeTable/LifeTablePage";
import CountryPage from "../pages/country/CountryPage";
import ComparisonPage from "../pages/comparison/ComparisonPage";
import CausesPage from "../pages/causes/CausesPage";
import AboutPage from "../pages/about/AboutPage";

const AppRouter = () => {
  return (
    <BrowserRouter>
      <PageContainer>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/mortality" element={<MortalityPage />} />
          <Route path="/life-table" element={<LifeTablePage />} />
          <Route path="/population" element={<PopulationPage />} />
          <Route path="/prediction" element={<PredictionPage />} />
          <Route path="/donation" element={<DonationPage />} />
          <Route path="/country" element={<CountryPage />} />
          <Route path="/comparison" element={<ComparisonPage />} />
          <Route path="/causes" element={<CausesPage />} />
          <Route path="/about" element={<AboutPage/>} />
        </Routes>
      </PageContainer>
    </BrowserRouter>
  );
};

export default AppRouter;