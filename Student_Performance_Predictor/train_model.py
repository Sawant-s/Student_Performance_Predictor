# ==============================================================
# train_model.py
# Student Performance Predictor - Model Training File
# --------------------------------------------------------------
# This file trains 3 Machine Learning models, compares them,
# and saves the BEST model so that app.py can use it later.
#
# Simple steps followed in this file:
# 1. Import libraries
# 2. Load dataset
# 3. Explore dataset (basic info, missing values, duplicates)
# 4. Select input features (X) and output/target (y)
# 5. Split data into training and testing sets
# 6. Train 3 models
# 7. Compare models using R2 Score and MAE
# 8. Select the best model
# 9. Save the best model as a .pkl file
# 10. Create simple graphs
# ==============================================================

# ---------- 1. Import required libraries ----------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

print("=" * 60)
print("STUDENT PERFORMANCE PREDICTOR - MODEL TRAINING")
print("=" * 60)

# ---------- 2. Load the dataset ----------
DATA_PATH = "dataset/student_performance.csv"
data = pd.read_csv(DATA_PATH)

print("\nStep 1: Dataset Loaded Successfully")
print(f"Dataset Shape: {data.shape[0]} rows, {data.shape[1]} columns")

# ---------- 3. Display basic dataset information ----------
print("\nStep 2: Basic Dataset Information")
print(data.info())

print("\nFirst 5 rows of the dataset:")
print(data.head())

# ---------- 4. Check missing values ----------
print("\nStep 3: Checking Missing Values")
missing_values = data.isnull().sum()
print(missing_values)

# If there are any missing values, fill them with the column average (mean).
# This keeps the code simple and beginner-friendly.
if data.isnull().values.any():
    data = data.fillna(data.mean(numeric_only=True))
    print("Missing values were found and filled with column averages.")
else:
    print("No missing values found. Good to go!")

# ---------- 5. Check duplicate records ----------
print("\nStep 4: Checking Duplicate Records")
duplicate_count = data.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_count}")

if duplicate_count > 0:
    data = data.drop_duplicates()
    print("Duplicate rows removed.")
else:
    print("No duplicate rows found.")

# ---------- 6. Select input features (X) and target (y) ----------
# NOTE: These column names MUST match the input fields used in app.py
FEATURE_COLUMNS = [
    "Study_Hours",
    "Attendance",
    "Previous_Marks",
    "Assignment_Marks",
    "Internal_Marks",
    "Practical_Marks",
    "Backlogs"
]

TARGET_COLUMN = "Final_Marks"

X = data[FEATURE_COLUMNS]
y = data[TARGET_COLUMN]

print("\nStep 5: Features and Target Selected")
print(f"Input Features: {FEATURE_COLUMNS}")
print(f"Target Column: {TARGET_COLUMN}")

# ---------- 7. Split data into training and testing sets ----------
# 80% data for training, 20% data for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nStep 6: Data Split Completed")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# ---------- 8. Train the 3 Machine Learning Models ----------
print("\nStep 7: Training Machine Learning Models...")

# Model 1: Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
linear_predictions = linear_model.predict(X_test)

# Model 2: Decision Tree Regressor
tree_model = DecisionTreeRegressor(max_depth=6, random_state=42)
tree_model.fit(X_train, y_train)
tree_predictions = tree_model.predict(X_test)

# Model 3: Random Forest Regressor
forest_model = RandomForestRegressor(n_estimators=150, max_depth=8, random_state=42)
forest_model.fit(X_train, y_train)
forest_predictions = forest_model.predict(X_test)

print("All 3 models trained successfully!")

# ---------- 9. Calculate R2 Score and MAE for each model ----------
print("\nStep 8: Evaluating Models on Test Data")

results = {
    "Linear Regression": {
        "model": linear_model,
        "r2": r2_score(y_test, linear_predictions),
        "mae": mean_absolute_error(y_test, linear_predictions)
    },
    "Decision Tree": {
        "model": tree_model,
        "r2": r2_score(y_test, tree_predictions),
        "mae": mean_absolute_error(y_test, tree_predictions)
    },
    "Random Forest": {
        "model": forest_model,
        "r2": r2_score(y_test, forest_predictions),
        "mae": mean_absolute_error(y_test, forest_predictions)
    }
}

# ---------- 10. Compare the models ----------
print("\n" + "=" * 60)
print("MODEL COMPARISON RESULTS (calculated from real test data)")
print("=" * 60)
print(f"{'Model':<20}{'R2 Score':>12}{'MAE':>12}")
print("-" * 44)
for model_name, values in results.items():
    print(f"{model_name:<20}{values['r2']:>12.4f}{values['mae']:>12.4f}")

# ---------- 11. Select the best model ----------
# We choose the model with the HIGHEST R2 Score
best_model_name = max(results, key=lambda name: results[name]["r2"])
best_model = results[best_model_name]["model"]
best_r2 = results[best_model_name]["r2"]
best_mae = results[best_model_name]["mae"]

print("\n" + "=" * 60)
print(f"BEST MODEL SELECTED: {best_model_name}")
print(f"R2 Score: {best_r2:.4f}")
print(f"MAE: {best_mae:.4f}")
print("=" * 60)

# ---------- 12. Save the best model ----------
os.makedirs("model", exist_ok=True)
MODEL_PATH = "model/student_performance_model.pkl"

joblib.dump({
    "model": best_model,
    "model_name": best_model_name,
    "features": FEATURE_COLUMNS,
    "r2_score": best_r2,
    "mae": best_mae,
    "all_results": {
        name: {"r2": v["r2"], "mae": v["mae"]} for name, v in results.items()
    }
}, MODEL_PATH)

print(f"\nBest model saved successfully at: {MODEL_PATH}")

# ---------- 13. Create simple graphs ----------
print("\nStep 9: Creating Graphs...")
os.makedirs("graphs", exist_ok=True)

# Graph 1: Study Hours vs Final Marks
plt.figure(figsize=(7, 5))
plt.scatter(data["Study_Hours"], data["Final_Marks"], color="#2E86AB", alpha=0.6)
plt.title("Study Hours vs Final Marks")
plt.xlabel("Study Hours per Day")
plt.ylabel("Final Marks")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("graphs/study_hours_vs_marks.png")
plt.close()

# Graph 2: Attendance vs Final Marks
plt.figure(figsize=(7, 5))
plt.scatter(data["Attendance"], data["Final_Marks"], color="#A23B72", alpha=0.6)
plt.title("Attendance vs Final Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Marks")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("graphs/attendance_vs_marks.png")
plt.close()

# Graph 3: Previous Marks vs Final Marks
plt.figure(figsize=(7, 5))
plt.scatter(data["Previous_Marks"], data["Final_Marks"], color="#F18F01", alpha=0.6)
plt.title("Previous Marks vs Final Marks")
plt.xlabel("Previous Exam Marks")
plt.ylabel("Final Marks")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("graphs/previous_marks_vs_marks.png")
plt.close()

# Graph 4: Assignment Marks vs Final Marks
plt.figure(figsize=(7, 5))
plt.scatter(data["Assignment_Marks"], data["Final_Marks"], color="#3B8686", alpha=0.6)
plt.title("Assignment Marks vs Final Marks")
plt.xlabel("Assignment Marks")
plt.ylabel("Final Marks")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("graphs/assignment_marks_vs_marks.png")
plt.close()

# Graph 5: Model Comparison (R2 Score)
plt.figure(figsize=(7, 5))
model_names = list(results.keys())
r2_values = [results[m]["r2"] for m in model_names]
bars = plt.bar(model_names, r2_values, color=["#2E86AB", "#F18F01", "#3B8686"])
plt.title("Model Comparison - R2 Score")
plt.xlabel("Model")
plt.ylabel("R2 Score")
plt.ylim(0, 1)
for bar, value in zip(bars, r2_values):
    plt.text(bar.get_x() + bar.get_width()/2, value + 0.01, f"{value:.3f}", ha="center")
plt.tight_layout()
plt.savefig("graphs/model_comparison.png")
plt.close()

print("Graphs saved successfully inside the 'graphs' folder.")

print("\n" + "=" * 60)
print("TRAINING COMPLETE! You can now run: streamlit run app.py")
print("=" * 60)
