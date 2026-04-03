// const HomePage = () => {
//   return (
//     <div>
//       <h1>Home</h1>
//       <p>This platform explores global mortality and population data.</p>
//     </div>
//   );
// };

// export default HomePage;



import HeroSection from "../../components/hero/HeroSection";
import LifePrediction from "../../components/prediction/LifePrediction";
const HomePage = () => {
  return (
    <>
      <HeroSection />

      <LifePrediction />
    </>
  );
}

export default HomePage;
