import time
import random
import json
from sklearn.cluster import KMeans
import numpy as np

print("====================================================")
print("  MACROSHIELD AMÉRICAS — COMPLIANCE-AUDITED BACKEND  ")
print("====================================================")


# 1. GENERATIVE SYNTHETIC DATA ENGINE
def generate_synthetic_crisis_logs(
    num_records=50,
    climate_stress=0.68,
    grid_strain=0.82
):
    """
    Generates anonymized infrastructure telemetry
    without capturing real civilian data.
    """

    synthetic_database = []

    for i in range(num_records):

        log_entry = {
            "mock_sector_id": f"SEC-{random.randint(10, 99)}",

            "timestamp_node": int(time.time()) + random.randint(1, 3600),

            "simulated_thermal_load": min(
                1.0,
                max(
                    0.0,
                    grid_strain + random.uniform(-0.15, 0.15)
                )
            ),

            "simulated_hydrological_pressure": min(
                1.0,
                max(
                    0.0,
                    climate_stress + random.uniform(-0.20, 0.20)
                )
            )
        }

        synthetic_database.append(log_entry)

    return synthetic_database


# 2. CORE ML PROCESSING LAYER
def evaluate_systemic_risk(logs):

    """
    Uses KMeans clustering to separate
    NOMINAL operational states from
    CRITICAL infrastructure anomalies.
    """

    features = np.array([
        [
            log["simulated_thermal_load"],
            log["simulated_hydrological_pressure"]
        ]
        for log in logs
    ])

    # KMeans ML Model
    kmeans = KMeans(
        n_clusters=2,
        random_state=42,
        n_init=10
    )

    predictions = kmeans.fit_predict(features)

    critical_count = np.sum(predictions == 1)
    nominal_count = np.sum(predictions == 0)

    print(
        f"\n[AI EVALUATOR AUDIT] "
        f"Evaluated {len(logs)} Synthetic Telemetry Rows."
    )

    print(
        f" -> Execution Telemetry: "
        f"{nominal_count} Nodes NOMINAL | "
        f"{critical_count} Nodes CRITICAL"
    )

    # HUMAN-IN-THE-LOOP CONSTRAINT GATE
    if critical_count > (len(logs) * 0.3):

        return {

            "status": "CRITICAL ANOMALY DETECTED",

            "recs": [
                "P1: Dispatch grid stabilization crews to Sector 13 substation.",

                "P2: Issue rolling-demand advisory to high-density districts."
            ],

            "hitl_state":
                "PAUSED — Awaiting Module 04 Manual "
                "'Approve & Deploy' Authorization Token."
        }

    else:

        return {

            "status": "NOMINAL",

            "recs": [
                "P3: Maintain background telemetry monitoring loops."
            ],

            "hitl_state":
                "NOMINAL — System operating within secure parameters."
        }


# MAIN PIPELINE
if __name__ == "__main__":

    print(
        "[PIPELINE START] "
        "Ingesting parameters from v0 frontend configuration sliders..."
    )

    # Simulated frontend slider values
    mock_climate = 0.68
    mock_grid = 0.82

    print(
        "[LAYER 1] "
        "Compiling Generative Synthetic Matrix "
        "(Privacy Shield Active)..."
    )

    simulated_data = generate_synthetic_crisis_logs(
        num_records=50,
        climate_stress=mock_climate,
        grid_strain=mock_grid
    )

    # OPTIONAL SAMPLE LOG OUTPUT
    print("\n[SYNTHETIC TELEMETRY SAMPLE]")
    print(json.dumps(simulated_data[:2], indent=2))

    print(
        "\n[LAYER 2] "
        "Triggering ML Clustering Analysis Matrix..."
    )

    pipeline_output = evaluate_systemic_risk(simulated_data)

    print("\n====================================================")
    print("  STAGED RECOMMENDATIONS PANEL (MODULE 03)          ")
    print("====================================================")

    print(
        f"System Operational Status: "
        f"{pipeline_output['status']}"
    )

    for rec in pipeline_output['recs']:
        print(f"  {rec}")

    print(
        f"\n[HUMAN-IN-THE-LOOP CONSTRAINT GATE]: "
        f"{pipeline_output['hitl_state']}"
    )

    print("====================================================")