# Iris Flower Classification App (Streamlit + Machine Learning)

## 📌 Project Overview

This project is a **Machine Learning web application** that classifies iris flowers into three species:

* Setosa
* Versicolor
* Virginica

The system uses the **K-Nearest Neighbors (KNN)** algorithm and is deployed using **Streamlit** to provide an interactive user interface.

---

## 🚀 Features

* 🌿 Interactive sliders for input features
* 🤖 Real-time prediction using trained ML model
* 📊 Model evaluation (Accuracy, Precision, Recall, F1-score)
* 📋 Clean classification report displayed in UI
* 🎨 Simple and user-friendly Streamlit interface

---

## 📊 Model Details

* Algorithm: K-Nearest Neighbors (KNN)
* k value: 5
* Evaluation metrics:

  * Accuracy
  * Classification Report

---

## ▶️ How to Run the Project

### 1. Install dependencies

```bash
pip install streamlit scikit-learn pandas numpy
```

### 2. Run the application

```bash
streamlit run app.py
```

---

## 📈 Output

The application provides:

* Predicted Iris flower species
* Model accuracy score
* Classification report in tabular form

---

## Learning Outcomes

After completing this project, the following skills and concepts were developed:

Understanding of the complete Machine Learning pipeline, including data preprocessing, model training, and evaluation.
Practical experience in implementing classification algorithms (KNN) using Scikit-learn.
Ability to build and deploy an interactive ML web application using Streamlit.

---

## 🎯 Future Improvements

* Add confusion matrix visualization
* Try advanced models (SVM, Random Forest)
* Deploy on cloud (Streamlit Cloud / Heroku)
* Add dataset visualization dashboard
