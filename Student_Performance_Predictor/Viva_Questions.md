# Viva Questions and Answers
## Student Performance Predictor Using AI/ML

**1. What is Machine Learning?**
Machine Learning is a part of Artificial Intelligence where a computer learns patterns from data and makes predictions, instead of being programmed with fixed rules.

**2. Why is Machine Learning used in this project?**
Because student performance depends on many factors together (study hours, attendance, past marks). ML can learn the relationship between these factors and final marks automatically from data.

**3. What is the aim of the project?**
To predict a student's final marks and performance level using their academic details, and to give simple suggestions for improvement.

**4. What is the dataset used in this project?**
It is a sample dataset created for academic use, containing 500 student records with details like study hours, attendance, previous marks, and final marks.

**5. What is training data?**
Training data is the part of the dataset (80% in this project) used to teach the Machine Learning model the relationship between inputs and final marks.

**6. What is testing data?**
Testing data is the remaining part of the dataset (20% in this project) that is not shown to the model during training. It is used to check how well the model performs on new, unseen data.

**7. What is Linear Regression?**
Linear Regression is a Machine Learning algorithm that finds a simple straight-line relationship between the input features and the final marks.

**8. What is a Decision Tree?**
A Decision Tree is an algorithm that makes predictions by splitting data using simple yes/no conditions, similar to a flowchart.

**9. What is Random Forest?**
Random Forest is an algorithm that builds many Decision Trees and combines their results to give a more accurate and stable prediction.

**10. Why did you compare three models instead of using just one?**
To find out which algorithm gives the most accurate prediction for this specific dataset, instead of assuming one algorithm is always best.

**11. What is R² Score?**
R² Score tells us how well the model's predictions match the actual values. A score closer to 1 means the model explains the data very well.

**12. What is MAE (Mean Absolute Error)?**
MAE is the average difference between the predicted marks and the actual marks. A lower MAE means the predictions are closer to the real values.

**13. Why did you select the best model based on R² Score?**
Because a higher R² Score means the model's predictions are closer to the real final marks, showing better overall accuracy.

**14. How does the prediction work in this project?**
The user enters student details in the web form. This data is passed to the saved trained model, which returns a predicted final marks value.

**15. What is Streamlit?**
Streamlit is a Python library used to quickly build interactive web applications for data science and Machine Learning projects, without needing HTML or JavaScript.

**16. Why did you use Python for this project?**
Python is simple to write and read, and it has powerful libraries like Pandas, Scikit-learn, and Matplotlib that make Machine Learning projects easy to build.

**17. What are the inputs to this system?**
Study hours, attendance percentage, previous marks, assignment marks, internal marks, practical marks, and number of backlogs.

**18. What is the output of this system?**
The predicted final marks, the performance level (Poor/Average/Good/Excellent), and simple suggestions for improvement.

**19. What are the limitations of this project?**
It uses a sample dataset instead of real student records, and it does not consider factors like health or family background that can also affect performance.

**20. What can be added in the future?**
Real institutional data, subject-wise predictions, a login system, online deployment, and integration with college management systems.

**21. Why did you remove duplicate and missing values from the dataset?**
Duplicate and missing values can confuse the model and reduce accuracy, so cleaning the data ensures the model learns from correct, unique information.

**22. Why is the dataset split into training and testing sets?**
To fairly evaluate how well the model performs on data it has never seen before, instead of just checking performance on data it was trained on.

**23. What is joblib used for in this project?**
Joblib is used to save the trained Machine Learning model to a file (.pkl) so it can be loaded later in the Streamlit app without retraining it every time.
