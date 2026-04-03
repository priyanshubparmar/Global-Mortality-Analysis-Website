import { useEffect, useState } from "react";
import profile from "../../assets/priyanshu.jpg";
import { FaMapMarkerAlt } from "react-icons/fa";
const scrollToPrediction = () => {
  const section = document.getElementById("lifePrediction");
  section?.scrollIntoView({ behavior: "smooth" });
};

const HeroSection = () => {

  const [shrink, setShrink] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 100) {
        setShrink(true);
      } else {
        setShrink(false);
      }
    };

    window.addEventListener("scroll", handleScroll);

    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <section className={`hero ${shrink ? "hero-small" : ""}`}>

      <div className="hero-card">

        <div className="hero-content">

          <div className="hero-text">
            <h1>  Hi, I'm Priyanshu B. Parmar</h1>

            <h3>  Applied Statistics Student 2024-26</h3>
            <h3 className="location">
                <FaMapMarkerAlt className="location-icon" />
                <a
                    href="https://www.spuvvn.edu/academics/departments/statistics/"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                      From the Department of Statistics, Sardar Patel University
                </a>
            </h3>
            <p>
                This is the platform where every one can explore global mortality trends, compare different country and predictive life expectancy.
            </p>
          </div>

          <div className="hero-image">
            <img src={profile} alt="Priyanshu Parmar" />
          </div>

        </div>

      </div>

      <div className="hero-buttons">
        <button className="hero-btn primary" onClick={scrollToPrediction}>
          Know Your Remaining Age
        </button>

        <button className="hero-btn">
          Know About Your Country
        </button>

        <button className="hero-btn">
          Compare Two Countries
        </button>
      </div>

    </section>
  );
};

export default HeroSection;