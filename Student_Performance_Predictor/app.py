# ==============================================================
# app.py
# Student Performance Predictor - Streamlit Web Application
# ==============================================================
# This app has 5 pages (using a sidebar):
# 1. Home
# 2. Prediction
# 3. Dashboard
# 4. ML Model
# 5. About
# ==============================================================

import streamlit as st
import pandas as pd
import joblib
import os

# --------------------------------------------------------------
# Page Configuration
# --------------------------------------------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------------------
# Simple custom styling (kept minimal and clean)
# --------------------------------------------------------------
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #2E86AB;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 20px;
        color: #6c757d;
        margin-top: 0px;
    }
    .card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e9ecef;
        text-align: center;
    }
    .result-box {
        background-color: #f0f7ff;
        padding: 25px;
        border-radius: 15px;
        border-left: 6px solid #2E86AB;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------------------
# File paths
# --------------------------------------------------------------
DATA_PATH = "dataset/student_performance.csv"
MODEL_PATH = "model/student_performance_model.pkl"

# --------------------------------------------------------------
# Helper Function: Load dataset (cached so it loads only once)
# --------------------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

# --------------------------------------------------------------
# Helper Function: Load trained model (cached so it loads only once)
# --------------------------------------------------------------
@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    return joblib.load(MODEL_PATH)

# --------------------------------------------------------------
# Helper Function: Decide performance level from marks
# --------------------------------------------------------------
def get_performance_level(marks):
    if marks < 40:
        return "Poor", "🔴"
    elif marks < 60:
        return "Average", "🟠"
    elif marks < 75:
        return "Good", "🟡"
    else:
        return "Excellent", "🟢"

# --------------------------------------------------------------
# Helper Function: Generate simple suggestions
# --------------------------------------------------------------
def get_suggestions(study_hours, attendance, previous_marks,
                     assignment_marks, backlogs, performance_level):
    suggestions = []

    if study_hours < 3:
        suggestions.append("Try to study for more time every day.")
    if attendance < 75:
        suggestions.append("Try to improve your attendance.")
    if previous_marks < 50:
        suggestions.append("Spend more time on revision and practice.")
    if assignment_marks < 50:
        suggestions.append("Try to complete assignments regularly.")
    if backlogs > 0:
        suggestions.append("Try to clear your pending subjects.")

    if len(suggestions) == 0:
        suggestions.append("Keep studying regularly and maintain your attendance.")

    if performance_level == "Excellent" and len(suggestions) == 1:
        suggestions.append("Keep working regularly and maintain your performance.")

    return suggestions

# --------------------------------------------------------------
# Helper Function: Simple input validation
# --------------------------------------------------------------
def validate_inputs(name, study_hours, attendance, previous_marks,
                     assignment_marks, internal_marks, practical_marks, backlogs):
    errors = []

    if name.strip() == "":
        errors.append("Student name should not be empty.")
    if study_hours < 0:
        errors.append("Study hours should not be negative.")
    if not (0 <= attendance <= 100):
        errors.append("Attendance must be between 0 and 100.")
    for label, value in [("Previous Marks", previous_marks),
                          ("Assignment Marks", assignment_marks),
                          ("Internal Marks", internal_marks),
                          ("Practical Marks", practical_marks)]:
        if not (0 <= value <= 100):
            errors.append(f"{label} must be between 0 and 100.")
    if backlogs < 0:
        errors.append("Backlogs should not be negative.")

    return errors

# --------------------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------------------
st.sidebar.title("🎓 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "👨‍🎓 Prediction", "📊 Dashboard", "🤖 ML Model", "ℹ️ About"]
)

# ================================================================
# PAGE 1: HOME
# ================================================================
if page == "🏠 Home":
    st.markdown('<p class="main-title">Student Performance Predictor</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Predict • Analyze • Improve</p>', unsafe_allow_html=True)
    st.write("")

    st.write(
        "This application uses Machine Learning to predict student performance "
        "based on academic information."
    )

    if st.button("🔮 Start Prediction", type="primary"):
        st.info("Please select '👨‍🎓 Prediction' from the sidebar to continue.")

    st.write("")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>🤖</h3>
        <h4>AI/ML Based</h4>
        <p>Uses trained Machine Learning models to predict marks.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>✅</h3>
        <h4>Easy to Use</h4>
        <p>Simple form-based input, no technical knowledge needed.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>🎓</h3>
        <h4>Student Friendly</h4>
        <p>Built for students and teachers to track performance.</p>
        </div>
        """, unsafe_allow_html=True)

# ================================================================
# PAGE 2: PREDICTION
# ================================================================
elif page == "👨‍🎓 Prediction":
    st.markdown('<p class="main-title">Predict Student Performance</p>', unsafe_allow_html=True)
    st.write("Fill in the student details below and click **Predict Performance**.")
    st.write("")

    model_data = load_model()

    if model_data is None:
        st.error("Model not found. Please run 'python train_model.py' first.")
    else:
        col1, col2 = st.columns(2)

        with col1:
            student_name = st.text_input("Student Name", placeholder="Enter student name")
            study_hours = st.slider("Study Hours per Day", 0.0, 12.0, 4.0, 0.5)
            attendance = st.slider("Attendance Percentage (%)", 0, 100, 75)
            previous_marks = st.number_input("Previous Exam Marks", 0, 100, 65)

        with col2:
            assignment_marks = st.number_input("Assignment Marks", 0, 100, 70)
            internal_marks = st.number_input("Internal Marks", 0, 100, 68)
            practical_marks = st.number_input("Practical Marks", 0, 100, 70)
            backlogs = st.selectbox("Number of Backlogs", [0, 1, 2, 3, 4, 5])

        st.write("")
        predict_clicked = st.button("🔮 Predict Performance", type="primary", use_container_width=True)

        if predict_clicked:
            errors = validate_inputs(
                student_name, study_hours, attendance, previous_marks,
                assignment_marks, internal_marks, practical_marks, backlogs
            )

            if errors:
                for error in errors:
                    st.error(error)
            else:
                # Build the input row in the SAME column order used during training
                input_df = pd.DataFrame([{
                    "Study_Hours": study_hours,
                    "Attendance": attendance,
                    "Previous_Marks": previous_marks,
                    "Assignment_Marks": assignment_marks,
                    "Internal_Marks": internal_marks,
                    "Practical_Marks": practical_marks,
                    "Backlogs": backlogs
                }])

                model = model_data["model"]
                predicted_marks = model.predict(input_df)[0]
                predicted_marks = round(float(max(0, min(100, predicted_marks))), 1)

                performance_level, emoji = get_performance_level(predicted_marks)
                suggestions = get_suggestions(
                    study_hours, attendance, previous_marks,
                    assignment_marks, backlogs, performance_level
                )

                st.write("---")
                st.markdown('<div class="result-box">', unsafe_allow_html=True)

                st.subheader(f"Results for: {student_name}")

                result_col1, result_col2 = st.columns(2)
                with result_col1:
                    st.metric("Predicted Final Marks", f"{predicted_marks}%")
                with result_col2:
                    st.metric("Performance Level", f"{emoji} {performance_level}")

                st.progress(int(predicted_marks))

                st.markdown("#### 💡 Suggestions")
                for suggestion in suggestions:
                    st.write(f"- {suggestion}")

                st.markdown('</div>', unsafe_allow_html=True)

                st.write("")
                st.markdown("#### 📋 Entered Details")

                d1, d2, d3, d4 = st.columns(4)
                d1.metric("Study Hours", f"{study_hours} hrs/day")
                d2.metric("Attendance", f"{attendance}%")
                d3.metric("Previous Marks", f"{previous_marks}%")
                d4.metric("Assignment Marks", f"{assignment_marks}%")

                d5, d6, d7 = st.columns(3)
                d5.metric("Internal Marks", f"{internal_marks}%")
                d6.metric("Practical Marks", f"{practical_marks}%")
                d7.metric("Backlogs", backlogs)

# ================================================================
# PAGE 3: DASHBOARD
# ================================================================
elif page == "📊 Dashboard":
    st.markdown('<p class="main-title">Dashboard</p>', unsafe_allow_html=True)
    st.write("Overview of the student dataset used to train the ML model.")
    st.write("")

    data = load_data()

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Students", len(data))
    c2.metric("Average Final Marks", f"{data['Final_Marks'].mean():.1f}%")
    c3.metric("Highest Marks", f"{data['Final_Marks'].max():.0f}%")

    c4, c5, c6 = st.columns(3)
    c4.metric("Lowest Marks", f"{data['Final_Marks'].min():.0f}%")
    c5.metric("Average Attendance", f"{data['Attendance'].mean():.1f}%")
    c6.metric("Average Study Hours", f"{data['Study_Hours'].mean():.1f} hrs/day")

    st.write("")
    st.markdown("#### 📈 Data Graphs")

    graph_files = {
        "Study Hours vs Final Marks": "graphs/study_hours_vs_marks.png",
        "Attendance vs Final Marks": "graphs/attendance_vs_marks.png",
        "Previous Marks vs Final Marks": "graphs/previous_marks_vs_marks.png",
        "Assignment Marks vs Final Marks": "graphs/assignment_marks_vs_marks.png",
    }

    g_col1, g_col2 = st.columns(2)
    columns = [g_col1, g_col2]

    for index, (title, path) in enumerate(graph_files.items()):
        with columns[index % 2]:
            st.markdown(f"**{title}**")
            if os.path.exists(path):
                st.image(path, use_container_width=True)
            else:
                st.warning("Graph not found. Please run train_model.py first.")

    st.write("")
    st.markdown("#### 🗂️ Sample Data")
    st.dataframe(data.head(10), use_container_width=True)

# ================================================================
# PAGE 4: ML MODEL
# ================================================================
elif page == "🤖 ML Model":
    st.markdown('<p class="main-title">Machine Learning Models</p>', unsafe_allow_html=True)
    st.write("Comparison of the three trained models on real test data.")
    st.write("")

    model_data = load_model()

    if model_data is None:
        st.error("Model not found. Please run 'python train_model.py' first.")
    else:
        results = model_data["all_results"]
        best_model_name = model_data["model_name"]

        comparison_df = pd.DataFrame([
            {"Model": name, "R2 Score": round(vals["r2"], 4), "MAE": round(vals["mae"], 4)}
            for name, vals in results.items()
        ])

        st.dataframe(comparison_df, use_container_width=True, hide_index=True)

        st.success(f"✅ Best Model Selected: **{best_model_name}** "
                   f"(R² Score: {results[best_model_name]['r2']:.4f}, "
                   f"MAE: {results[best_model_name]['mae']:.4f})")

        if os.path.exists("graphs/model_comparison.png"):
            st.image("graphs/model_comparison.png", use_container_width=True)

        st.write("")
        st.markdown("#### 📖 Simple Explanation of Each Algorithm")

        st.markdown("**Linear Regression**")
        st.write("It finds a simple relationship between student details and final marks.")

        st.markdown("**Decision Tree**")
        st.write("It makes decisions using simple conditions, like a flowchart.")

        st.markdown("**Random Forest**")
        st.write("It uses many decision trees and combines their results for a better prediction.")

# ================================================================
# PAGE 5: ABOUT
# ================================================================
elif page == "ℹ️ About":
    st.markdown('<p class="main-title">About the Project</p>', unsafe_allow_html=True)
    st.write("")

    st.write(
        "The **Student Performance Predictor** is an AI/ML-based application that helps "
        "predict student final marks using academic information such as study hours, "
        "attendance, previous marks, and more."
    )

    st.markdown("#### 🛠️ Technologies Used")
    st.write("- Python\n- Streamlit\n- Pandas\n- NumPy\n- Scikit-learn\n- Matplotlib")

    st.markdown("#### 🤖 ML Algorithms")
    st.write("- Linear Regression\n- Decision Tree Regressor\n- Random Forest Regressor")

    st.markdown("#### 📌 Note")
    st.info("This project uses a sample dataset created for academic purposes only.")
