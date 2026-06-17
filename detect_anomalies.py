"""
W. Dominic Fernando - dominicfernando74@gmail.com
Detect failing wind turbines from telemetry data.

This script reads a telemetry CSV, calculates per-turbine metrics, and prints the
Turbine IDs that breach the anomaly rules:
  - average temperature above 85.0 C
  - vibration spiking above 15.0 mm/s

Usage:
    python detect_anomalies.py telemetry_data.csv
"""

import pandas as pd
import argparse

# Anomaly thresholds (a turbine fails if it breaches either temp OR vibration).
temp_anomaly = 85.0
vibration_anomaly = 15.0


def detect_anomalies(csv):
    df = pd.read_csv(csv)

    # I collapsed the raw readings down to one row per turbine.
    metrics = df.groupby("turbine_id").agg(
        temp_mean = ("temperature_c", "mean"),
        max_vibration_mm_s = ("vibration_mm_s", "max"),
    )

    # we flag each turbine against the two rules temps and vibration.
    metrics["temp_anomaly"] = metrics["temp_mean"] > temp_anomaly
    metrics["vibration_anomaly"] = metrics["max_vibration_mm_s"] > vibration_anomaly

    return metrics


def main():
    # Then we read the CSV path from the command line.
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    args = parser.parse_args()

    metrics = detect_anomalies(args.csv)

    # A turbine is failing if it breaks either rule.
    metrics["failing"] = metrics["temp_anomaly"] | metrics["vibration_anomaly"]
    failing = metrics[metrics["failing"]]

    if failing.empty:
        print("All turbines operating within safe limits. No anomalies detected.")
        return

    # after that we print each failing turbine with the reasons it failed.
    print("Failing turbines (urgent maintenance required):")
    for tid, row in failing.iterrows():
        reasons = []
        if row["temp_anomaly"]:
            reasons.append(f"avg temp {row['temp_mean']:.1f}C > {temp_anomaly}C")
        if row["vibration_anomaly"]:
            reasons.append(f"max vibration {row['max_vibration_mm_s']:.1f} mm/s > {vibration_anomaly} mm/s")
        print(f"  - {tid}: {', '.join(reasons)}")


if __name__ == "__main__":
    main()
