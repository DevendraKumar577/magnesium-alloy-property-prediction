
import pandas as pd
import numpy as np

# Load predicted mechanical properties
df = pd.read_csv("Y_composition_predictions.csv")

print("Dataset columns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

# Normalize mechanical properties
# Higher strength and hardness = better
# Lower creep rate = better

properties = [
    "Tensile_UTS_MPa_SYNTHETIC",
    "Compressive_Strength_MPa_SYNTHETIC",
    "Hardness_HV_SYNTHETIC",
    "Fatigue_Strength_MPa_SYNTHETIC"
]

for col in properties:
    min_val = df[col].min()
    max_val = df[col].max()

    df[col + "_score"] = (
        (df[col] - min_val) / (max_val - min_val)
    ) * 100

# Lower creep rate is better
col = "Creep_Rate_s-1_SYNTHETIC"

df[col + "_score"] = (
    (df[col].max() - df[col]) /
    (df[col].max() - df[col].min())
) * 100

# Calculate overall score
score_columns = [col + "_score" for col in properties]
score_columns.append("Creep_Rate_s-1_SYNTHETIC_score")

df["Overall_Performance_Score"] = df[score_columns].mean(axis=1)

# Save results
df.to_csv("overall_performance_results.csv", index=False)

# Find optimal Y concentration
best_row = df.loc[df["Overall_Performance_Score"].idxmax()]

print("\nOVERALL PERFORMANCE RESULTS")
print("Best Y Concentration:", best_row["Y_wt_pct"])
print("Overall Score:", round(best_row["Overall_Performance_Score"], 2))

print("\nResults saved successfully!")
