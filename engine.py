import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# --------------------------------------------------
# MACROSHIELD AMÉRICAS - SYNTHETIC AI ENGINE
# USAII Global AI Hackathon 2026
# --------------------------------------------------

np.random.seed(42)

# Generate synthetic infrastructure data
num_samples = 50

data = pd.DataFrame({
    "climate_stress": np.random.randint(20, 100, num_samples),
    "grid_strain": np.random.randint(20, 100, num_samples),
    "population_density": np.random.randint(10, 100, num_samples),
})

# Risk scoring formula
data["risk_score"] = (
    data["climate_stress"] * 0.35 +
    data["grid_strain"] * 0.45 +
    data["population_density"] * 0.20
)

# KMeans clustering
model = KMeans(n_clusters=3, random_state=42, n_init=10)

features = data[[
    "climate_stress",
    "grid_strain",
    "population_density",
    "risk_score"
]]

data["cluster"] = model.fit_predict(features)

# Map clusters to severity labels
cluster_risk = data.groupby("cluster")["risk_score"].mean().sort_values()

severity_map = {}

severity_map[cluster_risk.index[0]] = "Nominal"
severity_map[cluster_risk.index[1]] = "Elevated"
severity_map[cluster_risk.index[2]] = "Critical"

data["severity"] = data["cluster"].map(severity_map)

# Recommendation engine
def generate_recommendation(row):
    if row["severity"] == "Critical":
        return "Dispatch stabilization crews immediately"
    elif row["severity"] == "Elevated":
        return "Increase monitoring and prepare contingency plans"
    else:
        return "Maintain nominal operations"

data["recommendation"] = data.apply(generate_recommendation, axis=1)

# Display results
print("\n--- MACROSHIELD SYNTHETIC ANALYSIS ---\n")

for idx, row in data.head(10).iterrows():
    print(f"Sector {idx + 1}")
    print(f"Climate Stress: {row['climate_stress']}")
    print(f"Grid Strain: {row['grid_strain']}")
    print(f"Population Density: {row['population_density']}")
    print(f"Risk Score: {round(row['risk_score'], 2)}")
    print(f"Severity: {row['severity']}")
    print(f"Recommendation: {row['recommendation']}")
    print("-" * 50)

print("\nSynthetic analysis complete.")
