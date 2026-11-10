# generate_dataset.py
# ------------------------------------------------------------
# This script creates a SAMPLE dataset for academic use.
# It is NOT real student data. It is generated using simple
# rules so that Study Hours, Attendance, Previous Marks, etc.
# have a realistic relationship with Final Marks.
# ------------------------------------------------------------

import numpy as np
import pandas as pd

# Fix the random seed so results are the same every time we run this file
np.random.seed(42)

NUM_STUDENTS = 500

# ---- Step 1: Create input features with realistic ranges ----

study_hours = np.round(np.random.normal(loc=4.5, scale=1.8, size=NUM_STUDENTS), 1)
study_hours = np.clip(study_hours, 0.5, 10)

attendance = np.round(np.random.normal(loc=78, scale=12, size=NUM_STUDENTS), 0)
attendance = np.clip(attendance, 40, 100)

previous_marks = np.round(np.random.normal(loc=65, scale=15, size=NUM_STUDENTS), 0)
previous_marks = np.clip(previous_marks, 20, 100)

assignment_marks = np.round(np.random.normal(loc=70, scale=13, size=NUM_STUDENTS), 0)
assignment_marks = np.clip(assignment_marks, 20, 100)

internal_marks = np.round(np.random.normal(loc=68, scale=13, size=NUM_STUDENTS), 0)
internal_marks = np.clip(internal_marks, 20, 100)

practical_marks = np.round(np.random.normal(loc=72, scale=12, size=NUM_STUDENTS), 0)
practical_marks = np.clip(practical_marks, 20, 100)

# Backlogs are mostly 0, sometimes 1-3 (weighted so most students have 0)
backlogs = np.random.choice([0, 1, 2, 3], size=NUM_STUDENTS, p=[0.65, 0.2, 0.1, 0.05])

# ---- Step 2: Create Final Marks using a realistic formula ----
# Final marks depend mostly on study habits, attendance and past performance.
# We add small random noise so the data feels real, not perfectly predictable.

final_marks = (
    (study_hours * 4.2) +          # more study hours -> higher marks
    (attendance * 0.25) +          # better attendance -> higher marks
    (previous_marks * 0.25) +      # past performance matters
    (assignment_marks * 0.15) +
    (internal_marks * 0.15) +
    (practical_marks * 0.10) -
    (backlogs * 4.0) +             # backlogs reduce final marks
    np.random.normal(0, 4, NUM_STUDENTS)   # small random noise
)

final_marks = np.round(np.clip(final_marks, 0, 100), 0)

# ---- Step 3: Build the final table ----

student_ids = [f"STU{i+1:04d}" for i in range(NUM_STUDENTS)]

df = pd.DataFrame({
    "Student_ID": student_ids,
    "Study_Hours": study_hours,
    "Attendance": attendance,
    "Previous_Marks": previous_marks,
    "Assignment_Marks": assignment_marks,
    "Internal_Marks": internal_marks,
    "Practical_Marks": practical_marks,
    "Backlogs": backlogs,
    "Final_Marks": final_marks
})

# ---- Step 4: Save dataset ----
df.to_csv("dataset/student_performance.csv", index=False)

print("Sample dataset created successfully!")
print("File saved at: dataset/student_performance.csv")
print(f"Total records: {len(df)}")
print(df.head())
