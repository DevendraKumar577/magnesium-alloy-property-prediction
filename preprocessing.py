
import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Load dataset
df = pd.read_excel("Mg_Zn_Zr_Y_synthetic_demo_1000.xlsx")

# 2. Define input features
X = df[["Y_wt_pct"]]

# 3. Define target variables
y = df[
    [
        "Tensile_UTS_MPa_SYNTHETIC",
        "Compressive_Strength_MPa_SYNTHETIC",
        "Hardness_HV_SYNTHETIC",
        "Fatigue_Strength_MPa_SYNTHETIC",
        "Creep_Rate_s-1_SYNTHETIC"
    ]
]

# 4. Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# 5. Display dataset information
print("Input Features:", X.columns.tolist())
print("\nTarget Variables:", y.columns.tolist())

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

print("\nTraining Target Shape:", y_train.shape)
print("Testing Target Shape:", y_test.shape)

# 6. Save datasets
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)

y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("\nPreprocessing completed successfully!")
