# College Project Documentation
## Student Performance Predictor Using AI/ML

---

## 1. Abstract
Predicting student performance early can help teachers and students take timely action to improve results. This project uses Machine Learning to predict a student's final marks based on academic details like study hours, attendance, previous marks, and assignment scores. A simple and interactive web application is built using Streamlit so that anyone — student, teacher, or parent — can use it without technical knowledge. The system also classifies the performance level and gives simple suggestions for improvement.

## 2. Introduction
Academic performance depends on many factors such as regular study, attendance, and consistency in assignments and internal exams. Traditionally, performance is judged only after final exams, which is too late to make improvements. This project applies Machine Learning to predict performance in advance, so that corrective steps can be taken early.

## 3. Aim
To design and develop a Machine Learning based web application that predicts a student's final marks and performance level using their academic data.

## 4. Objectives
- To collect and prepare a dataset containing student academic details.
- To train and compare multiple Machine Learning models.
- To select the best-performing model based on real evaluation metrics.
- To build a simple, user-friendly Streamlit web application.
- To provide performance-based suggestions for improvement.

## 5. Problem Statement
Students and teachers often do not know how a student is likely to perform until final results are declared. There is no simple tool that uses existing academic data (study hours, attendance, past marks) to estimate future performance and suggest improvements in advance.

## 6. Existing System
Currently, performance prediction is usually done manually by teachers based on experience and observation. This is subjective, inconsistent, and does not scale to large classrooms. There is no automated, data-driven prediction system commonly used in colleges.

## 7. Proposed System
The proposed system uses Machine Learning algorithms trained on academic data to predict final marks automatically. The system:
- Takes structured input from the user through a web form.
- Uses a trained ML model to predict final marks.
- Classifies performance into Poor, Average, Good, or Excellent.
- Provides simple, actionable suggestions.

## 8. Scope
The project is designed as an academic mini-project. It works on a sample dataset and can be extended in the future to real institutional data, multiple subjects, semester-wise tracking, and integration with college management systems.

## 9. Hardware Requirements
- A computer/laptop with at least 4 GB RAM
- 1 GB free disk space
- Standard keyboard, mouse, and monitor

## 10. Software Requirements
- Operating System: Windows 10 or above
- Python 3.9 or above
- Visual Studio Code (VS Code)
- Web Browser (Chrome/Edge/Firefox)
- Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Streamlit, Joblib

## 11. System Architecture
```
   [User Input Form - Streamlit UI]
                |
                v
   [Input Validation & Processing]
                |
                v
   [Trained ML Model (.pkl file)]
                |
                v
   [Predicted Marks + Performance Level + Suggestions]
                |
                v
       [Displayed on Web Interface]
```

## 12. Modules
1. **Data Collection & Preprocessing Module** — Loads, cleans, and prepares the dataset.
2. **Model Training Module (`train_model.py`)** — Trains and compares ML models, saves the best one.
3. **Prediction Module** — Takes user input and predicts final marks.
4. **Dashboard Module** — Displays dataset statistics and graphs.
5. **Suggestion Module** — Generates simple improvement tips.
6. **User Interface Module (`app.py`)** — Streamlit-based web interface with 5 pages.

## 13. Methodology
1. Collect/generate a structured dataset of student academic records.
2. Clean the data (handle missing values, remove duplicates).
3. Split the data into training (80%) and testing (20%) sets.
4. Train three regression models: Linear Regression, Decision Tree, Random Forest.
5. Evaluate each model using R² Score and Mean Absolute Error (MAE) on the test data.
6. Select and save the best-performing model.
7. Build a Streamlit web app that loads the saved model and predicts marks for new input.

## 14. Dataset Description
The dataset (`student_performance.csv`) is a **sample dataset created for academic use**, containing 500 student records with the following columns:

| Column | Description |
|---|---|
| Student_ID | Unique identifier for each student |
| Study_Hours | Average study hours per day |
| Attendance | Attendance percentage |
| Previous_Marks | Marks scored in the previous exam |
| Assignment_Marks | Marks scored in assignments |
| Internal_Marks | Marks scored in internal exams |
| Practical_Marks | Marks scored in practicals |
| Backlogs | Number of pending/failed subjects |
| Final_Marks | Target variable — final exam marks to be predicted |

## 15. Algorithms Used
- **Linear Regression** – Finds a straight-line relationship between input features and final marks.
- **Decision Tree Regressor** – Splits data using simple yes/no conditions to reach a prediction.
- **Random Forest Regressor** – Combines many decision trees to make a more accurate and stable prediction.

## 16. Testing
- **Unit Testing:** Each function (performance level, suggestions, validation) was tested with sample values.
- **Model Testing:** Models were evaluated on 20% unseen test data using R² Score and MAE.
- **Input Validation Testing:** Checked that invalid inputs (negative values, out-of-range marks, empty name) show proper error messages.
- **UI Testing:** All 5 pages were checked for correct navigation and display.

## 17. Results
The three models were compared using R² Score (higher is better) and MAE (lower is better) on the test dataset. The model with the highest R² Score was automatically selected as the final model and saved for use in the application. (Exact scores are printed when `train_model.py` is run, since results are calculated from real data and may vary slightly with dataset changes.)

## 18. Advantages
- Simple and easy to use, even for non-technical users.
- Gives early insight into expected performance.
- Provides actionable suggestions, not just a number.
- Built using lightweight, beginner-friendly tools.
- Runs completely offline on a local machine.

## 19. Limitations
- Uses a sample dataset, not real institutional data.
- Predicts only final marks, not subject-wise performance.
- Does not account for factors like health, family background, or extracurriculars.
- Accuracy depends on the quality and size of the dataset.

## 20. Future Scope
- Train on real, larger institutional datasets.
- Add subject-wise and semester-wise predictions.
- Add a login system for students and teachers.
- Deploy the application online for wider access.
- Integrate with existing college management systems.

## 21. Conclusion
The Student Performance Predictor demonstrates how Machine Learning can be applied to a real academic problem in a simple, understandable way. By comparing multiple models and selecting the best one based on real test results, the project follows correct ML practices while remaining easy to explain in a viva. It successfully predicts student performance and provides helpful, simple suggestions for improvement.
