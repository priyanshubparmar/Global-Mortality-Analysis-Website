import { useEffect, useState, useRef } from "react";
import Select from "react-select";
import { getFilters, getLifeTableAnalysis } from "../../services/lifeTableService";
import "../../styles/prediction.css";
import SurvivalChart from "../charts/SurvivalChart";
export default function LifePrediction() {

  const [filters, setFilters] = useState<any>(null);

  const [location, setLocation] = useState<any>(null);
  const [gender, setGender] = useState<any>(null);
  const [year, setYear] = useState<any>(null);
  const [age, setAge] = useState<any>(null);

  const [result, setResult] = useState<any>(null);
  const resultsRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    async function loadFilters() {
      const data = await getFilters();
      setFilters(data);
    }
    loadFilters();
  }, []);

  const handlePredict = async () => {

    if (!location || !gender || !year || !age) {
        alert("Select all fields");
        return;
    }

    const res = await getLifeTableAnalysis(
        location.value,
        gender.value,
        year.value,
        age.value
    );

    setResult(res);

    setTimeout(() => {
        resultsRef.current?.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }, 100);

  };

  if (!filters) return <p>Loading filters...</p>;

  return (
    <section className="prediction-section" id="lifePrediction">

      <h2>Know Your Remaining Life</h2>

      <div className="filter-grid">

        <Select
          placeholder="Location"
          options={filters.locations.map((v: string) => ({ value: v, label: v }))}
          onChange={setLocation}
        />

        <Select
          placeholder="Gender"
          options={filters.genders.map((v: string) => ({ value: v, label: v }))}
          onChange={setGender}
        />

        <Select
          placeholder="Year"
          options={filters.years.map((v: number) => ({ value: v, label: v }))}
          onChange={setYear}
        />

        <Select
          placeholder="Age"
          options={filters.ages.map((v: number) => ({ value: v, label: v }))}
          onChange={setAge}
        />

      </div>

      <button className="predict-btn" onClick={handlePredict}>
        Predict Remaining Life
      </button>

      {result && (
        <div className="results-grid" ref={resultsRef}>
          <div className="result-card">
            <h3>Expected Life Remaining</h3>
            <p>
                {result.indicators.expected_life_remaining.toFixed(0)} 
                <span className="ci-note">  years ± {result.indicators.expected_life_uncertainty.toFixed(1)} (95% CI)</span>
            </p>
        </div>
        
        <div className="result-card">
          <h3>Expected Age for Death</h3>

          <p className="main-value">
            {result.indicators.expected_age_at_death.toFixed(0)}{" "}
            <span className="ci-range">
              ({result.indicators.expected_age_lower.toFixed(0)} –{" "}
              {result.indicators.expected_age_upper.toFixed(0)} years)
            </span>{" "}
          </p>

        </div>
          {/* <div className="result-card">
            <h3>Expected Life Remaining</h3>

            <p>
            {result.indicators.expected_life_remaining.toFixed(1)} years
            </p>
          </div>

        <div className="result-card">
            <h3>Uncertainty of Expected Life </h3>
            <p>
                ± {result.indicators.expected_life_uncertainty.toFixed(1)} years 
                <span className="ci-text">  (95% CI)</span>
            </p>
        </div> */}
        <div className="result-card">
            <h3>Healthy Life Remaining</h3>
            <p>
                {result.indicators.healthy_life_remaining.toFixed(0)} 
                <span className="ci-note"> years ± {result.indicators.healthy_life_uncertainty.toFixed(0)} (95% CI)</span>
            </p>
        </div>
        

        <div className="result-card">
            <h3>Prob. of Surviving 10 More Years</h3>
            <p>{(result.indicators.prob_survive_10_years * 100).toFixed(2)} %</p> 
        </div>

        {result && (
          <div className="chart-section">

            <h2>Survival Curve</h2>

            <p className="chart-description">
              Probability of surviving to each age given the selected country, gender, and year.
            </p>

            <SurvivalChart
              data={result.survival_table}
              currentAge={age.value}
            />

          </div>
        )}



        </div>
      )}

    </section>
  );
}