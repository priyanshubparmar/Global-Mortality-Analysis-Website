import numpy as np
import pandas as pd
from backend.database import run_query



def compute_life_table(df):

    df = df.sort_values("Age").reset_index(drop=True)

    # -----------------------------
    # Mortality rate
    # -----------------------------
    df["mx"] = df["Death"] / df["Population"]

    df["mx_se"] = np.sqrt(df["mx"] / df["Population"])
    df["mx_lower"] = df["mx"] - 1.96 * df["mx_se"]
    df["mx_upper"] = df["mx"] + 1.96 * df["mx_se"]

    # -----------------------------
    # Probability of death
    # -----------------------------
    df["qx"] = df["Death"] / (df["Population"] + 0.5 * df["Death"])

    df["qx_lower"] = df["mx_lower"] / (1 + 0.5 * df["mx_lower"])
    df["qx_upper"] = df["mx_upper"] / (1 + 0.5 * df["mx_upper"])

    df["px"] = 1 - df["qx"]

    # -----------------------------
    # Survivors
    # -----------------------------
    l0 = 100000
    df["lx"] = l0 * df["px"].shift(fill_value=1).cumprod()

    # -----------------------------
    # Person years lived
    # -----------------------------
    df["Lx"] = (df["lx"] + df["lx"].shift(-1)) / 2

    df.loc[len(df)-1, "Lx"] = df.loc[len(df)-1, "lx"] / df.loc[len(df)-1, "mx"]

    # -----------------------------
    # Total person years
    # -----------------------------
    df["Tx"] = df["Lx"][::-1].cumsum()[::-1]

    # -----------------------------
    # Life expectancy
    # -----------------------------
    df["ex"] = df["Tx"] / df["lx"]

    df["ex_se"] = df["ex"] * 0.05
    df["ex_lower"] = df["ex"] - 1.96 * df["ex_se"]
    df["ex_upper"] = df["ex"] + 1.96 * df["ex_se"]

    # -----------------------------
    # Survival probability
    # -----------------------------
    df["survival_probability"] = df["lx"] / 100000

    # -----------------------------
    # Hazard rate
    # -----------------------------
    df["hazard_rate"] = df["qx"] / (1 - 0.5 * df["qx"])

    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.fillna(0)

    return df



def get_life_table(location, gender, year, user_age):

    # --------------------------
    # 1. Load mortality data
    # --------------------------

    query = f"""
    SELECT
        Age,
        Death,
        Population
    FROM mortality_data
    WHERE location = '{location}'
    AND gender = '{gender}'
    AND Year = {year}
    ORDER BY Age
    """

    df = run_query(query)

    # --------------------------
    # 2. Compute life table
    # --------------------------

    life_table = compute_life_table(df)

    # --------------------------
    # 3. Load disability table
    # --------------------------

    disability = run_query("""
        SELECT Age, disability_rate
        FROM disability_data
        ORDER BY Age
    """)




    # merge disability data
    life_table = life_table.merge(disability, on="Age", how="left")

        # --------------------------
    # 4. Compute health index
    # --------------------------

    country_mx = life_table["mx"].mean()

    world_query = f"""
    SELECT Death / Population AS mx
    FROM mortality_data
    WHERE location='World'
    AND gender='{gender}'
    AND Year={year}
    """

    world_df = run_query(world_query)

    world_mx = world_df["mx"].mean()

    health_index = country_mx / world_mx

    # --------------------------
    # 5. Adjust disability
    # --------------------------

    life_table["adjusted_disability"] = (
        life_table["disability_rate"] * health_index
    )

    life_table["adjusted_disability"] = life_table["adjusted_disability"].clip(0, 1)


    # compute healthy person years
    life_table["HealthyLx"] = life_table["Lx"] * (1 - life_table["disability_rate"])

    # cumulative healthy years
    life_table["HealthyTx"] = life_table["HealthyLx"][::-1].cumsum()[::-1]

    # disability free life expectancy
    life_table["dfle"] = life_table["HealthyTx"] / life_table["lx"]
    life_table["dfle_se"] = life_table["dfle"] * 0.05

    life_table["dfle_lower"] = (
        life_table["dfle"] - 1.96 * life_table["dfle_se"]
    )

    life_table["dfle_upper"] = (
        life_table["dfle"] + 1.96 * life_table["dfle_se"]
    )

    # years with disability
    life_table["years_with_disability"] = life_table["ex"] - life_table["dfle"]
    
    
    # highlight user age
    user_row = life_table[life_table["Age"] == user_age]

    if len(user_row) > 0:
        user_row = user_row.iloc[0].to_dict()
    else:
        user_row = {}

        # -----------------------------
    # Current age row
    # -----------------------------
    user_row = life_table[life_table["Age"] == user_age]

    if len(user_row) > 0:
        user_row = user_row.iloc[0].to_dict()
    else:
        user_row = {}

    # -----------------------------
    # Survival table
    # -----------------------------
    survival_table = life_table[[
        "Age",
        "lx",
        "Population"
    ]].copy()

    survival_table["survival_probability"] = survival_table["lx"] / 100000

    survival_table["se"] = (
        (survival_table["survival_probability"] *
        (1 - survival_table["survival_probability"])) /
        survival_table["Population"]
    ) ** 0.5

    survival_table["lower"] = (
        survival_table["survival_probability"] -
        1.96 * survival_table["se"]
    )

    survival_table["upper"] = (
        survival_table["survival_probability"] +
        1.96 * survival_table["se"]
    )
    healthy_survival_table = life_table[[
        "Age",
        "lx",
        "Population",
        "adjusted_disability"
    ]].copy()

    healthy_survival_table["survival_probability"] = (
        healthy_survival_table["lx"] / 100000
    )

    healthy_survival_table["healthy_survival_probability"] = (
        healthy_survival_table["survival_probability"] *
        (1 - healthy_survival_table["adjusted_disability"])
    )
    healthy_survival_table["se"] = (
        healthy_survival_table["healthy_survival_probability"] *
        (1 - healthy_survival_table["healthy_survival_probability"]) /
        healthy_survival_table["Population"]
    ) ** 0.5

    healthy_survival_table["lower"] = (
        healthy_survival_table["healthy_survival_probability"] -
        1.96 * healthy_survival_table["se"]
    )

    healthy_survival_table["upper"] = (
        healthy_survival_table["healthy_survival_probability"] +
        1.96 * healthy_survival_table["se"]
    )
    # -----------------------------
    # Median survival age
    # -----------------------------
    median_row = survival_table[
        survival_table["survival_probability"] <= 0.5
    ]

    median_age = int(median_row.iloc[0]["Age"]) if len(median_row) else None
    healthy_life_ratio = user_row.get("dfle") / user_row.get("ex")
    future_age = user_age + 10

    future_row = life_table[life_table["Age"] == future_age]
    disability_ratio = (
        user_row.get("years_with_disability") /
        user_row.get("ex")
    )

    expected_life_uncertainty = (
        1.96 * user_row.get("ex_se")
        if user_row.get("ex_se") else None
    )

    healthy_life_uncertainty = (
        1.96 * user_row.get("dfle_se")
        if user_row.get("dfle_se") else None
    )

    # -----------------------------
    # Expected age at death
    # -----------------------------

    expected_age_at_death = user_age + user_row.get("ex")

    expected_age_lower = user_age + user_row.get("ex_lower")
    expected_age_upper = user_age + user_row.get("ex_upper")
    if len(future_row):
        prob_10yr = future_row.iloc[0]["lx"] / user_row["lx"]
    else:
        prob_10yr = None


    # -----------------------------
    # Indicators
    # -----------------------------
    indicators = {
        "median_survival_age": median_age,
        "expected_life_remaining": user_row.get("ex"),
        "expected_life_uncertainty": expected_life_uncertainty,
        "expected_age_at_death": expected_age_at_death,
        "expected_age_lower": expected_age_lower,
        "expected_age_upper": expected_age_upper,
        "healthy_life_remaining": user_row.get("dfle"),
        "healthy_life_uncertainty": healthy_life_uncertainty,
        "years_with_disability": user_row.get("years_with_disability"),
        "healthy_life_ratio": healthy_life_ratio,
        "disability_ratio": disability_ratio,
        "prob_survive_10_years": prob_10yr
    }

    # -----------------------------
    # Final API response
    # -----------------------------
    return {
        "status": "success",

        "current_age": user_row,

        "life_table": life_table.to_dict(orient="records"),

        "survival_table": survival_table.to_dict(orient="records"),

        "healthy_survival_table": healthy_survival_table.to_dict(orient="records"),

        "indicators": indicators
    }

    