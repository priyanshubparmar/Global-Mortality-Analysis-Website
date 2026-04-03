import { useEffect, useState } from "react";
import Select from "react-select";
import {
  getFilters,
  getLifeTableAnalysis,
} from "../../services/lifeTableService";


export default function LifeTablePage() {

  const [filters, setFilters] = useState<any>(null);

  const [location, setLocation] = useState<any>(null);
  const [gender, setGender] = useState<any>(null);
  const [year, setYear] = useState<any>(null);
  const [age, setAge] = useState<any>(null);

  const [data, setData] = useState<any>(null);

  useEffect(() => {
    async function loadFilters() {
      const res = await getFilters();
      setFilters(res);
    }

    loadFilters();
  }, []);

  const handleSubmit = async () => {

    if (!location || !gender || !year || !age) {
      alert("Please select all filters");
      return;
    }

    const res = await getLifeTableAnalysis(
      location.value,
      gender.value,
      year.value,
      age.value
    );

    setData(res);
  };

  if (!filters) return <p>Loading filters...</p>;

  return (
    <div>
      <h1>-----------Under Development------------</h1>
      <h2>Life Table Analysis</h2>

      {/* LOCATION */}
      <Select
        placeholder="Select Location"
        options={filters.locations.map((v: string) => ({
          value: v,
          label: v,
        }))}
        onChange={setLocation}
      />

      {/* GENDER */}
      <Select
        placeholder="Select Gender"
        options={filters.genders.map((v: string) => ({
          value: v,
          label: v,
        }))}
        onChange={setGender}
      />

      {/* YEAR */}
      <Select
        placeholder="Select Year"
        options={filters.years.map((v: number) => ({
          value: v,
          label: v,
        }))}
        onChange={setYear}
      />

      {/* AGE */}
      <Select
        placeholder="Select Age"
        options={filters.ages.map((v: number) => ({
          value: v,
          label: v,
        }))}
        onChange={setAge}
      />

      <button onClick={handleSubmit}>
        Run Analysis
      </button>

      {data && (
        <div>

          <h2>Results</h2>

          <p>Median Survival Age: {data.median_survival_age}</p>
          <p>Expected Life Remaining: {data.expected_life_remaining}</p>
          <p>Healthy Life Remaining: {data.healthy_life_remaining}</p>
          <p>Years With Disability: {data.years_with_disability}</p>
          <p>Healthy Life Ratio: {data.healthy_life_ratio}</p>

        </div>
      )}
    </div>
  );
}