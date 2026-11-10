# 🎓 Student Performance Predictor Using AI/ML

## 📌 Project Aim
To predict a student's final marks using Machine Learning, based on academic details such as study hours, attendance, and previous performance — and to give simple suggestions for improvement.

## 📖 Project Description
This is a college-level AI/ML mini project built with **Python** and **Streamlit**. A user enters a student's academic details into a simple web form, and a trained Machine Learning model predicts the student's expected final marks. The app also shows the performance level (Poor / Average / Good / Excellent) and gives easy, practical suggestions.

> **Note:** The dataset used in this project (`dataset/student_performance.csv`) is a **sample dataset created for academic use**. It is not real student data, but it is generated so that study hours, attendance, and past marks realistically affect the final marks.

## ✨ Features
- Clean, modern Streamlit web interface with a sidebar
- Home, Prediction, Dashboard, ML Model, and About pages
- Real-time marks prediction using a trained ML model
- Performance level classification (Poor / Average / Good / Excellent)
- Simple, rule-based improvement suggestions
- Dashboard with dataset statistics and graphs
- Model comparison table (Linear Regression vs Decision Tree vs Random Forest)
- Input validation with friendly error messages

## 🛠️ Technologies Used
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

## 🤖 ML Algorithms
1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

The model with the **best R² Score** on real test data is automatically selected and saved.

## 📁 Folder Structure
```
Student_Performance_Predictor/
│
├── dataset/
│   └── student_performance.csv
│
├── model/
│   └── student_performance_model.pkl
│
├── graphs/
│   ├── study_hours_vs_marks.png
│   ├── attendance_vs_marks.png
│   ├── previous_marks_vs_marks.png
│   ├── assignment_marks_vs_marks.png
│   └── model_comparison.png
│
├── generate_dataset.py
├── train_model.py
├── app.py
├── requirements.txt
├── README.md
├── Documentation.md
└── Viva_Questions.md
```

## 💻 Installation Steps (Windows + VS Code)

### Step 1: Install Python
Download and install Python from https://www.python.org/downloads/
While installing, make sure to check **"Add Python to PATH"**.

### Step 2: Create the Project Folder
Create a folder named `Student_Performance_Predictor` anywhere on your computer (e.g., Desktop).

### Step 3: Open the Folder in VS Code
Open VS Code → File → Open Folder → select `Student_Performance_Predictor`.

### Step 4: Create a Virtual Environment
Open the VS Code terminal (`Ctrl + ~`) and run:
```bash
python -m venv venv
```

### Step 5: Activate the Virtual Environment
In PowerShell, run:
```bash
venv\Scripts\Activate.ps1
```
If you get a permission error, run this once in PowerShell (as Administrator):
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating again. You should see `(venv)` at the start of your terminal line.

### Step 6: Install Required Libraries
```bash
pip install -r requirements.txt
```

### Step 7: Add All Project Files
Place `generate_dataset.py`, `train_model.py`, `app.py`, and the dataset/model/graphs folders inside your project folder (already provided).

## 🚀 How to Train the Model
Run this command in the terminal:
```bash
python train_model.py
```
This will:
- Load and clean the dataset
- Train 3 ML models
- Print R² Score and MAE for each model
- Save the best model as `model/student_performance_model.pkl`
- Save graphs inside the `graphs` folder

## ▶️ How to Run the Streamlit App
After training is complete, run:
```bash
streamlit run app.py
```
This will automatically open the app in your browser at `http://localhost:8501`.
If it does not open automatically, copy that link into your browser.

## 📊 Example Prediction
**Input:**
- Student Name: Rahul
- Study Hours: 6 hours/day
- Attendance: 88%
- Previous Marks: 72
- Assignment Marks: 85
- Internal Marks: 78
- Practical Marks: 82
- Backlogs: 0

**Output:**
- Predicted Marks: ~82%
- Performance: Excellent
- Suggestion: "Keep studying regularly and maintain your attendance."

*(Exact predicted value may vary slightly depending on the trained model.)*

## 🔮 Future Improvements
- Add login system for students and teachers
- Store prediction history in a database
- Add more input features (extracurricular activities, sleep hours, etc.)
- Deploy the app online using Streamlit Cloud
- Add email/PDF report generation for each prediction
