import pandas as pd
import numpy as np
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report 


# Load dataset
iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Scale data
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Create and train model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)

# UI Title
st.markdown(
    "<h1 style='text-align: center; color: #FFC0CB;'>🌸 Iris Flower Classification App</h1>",
    unsafe_allow_html=True
)
st.write("Enter flower measurements to predict species")

# Input sliders
sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width", 0.1, 2.5, 1.0)

# Prediction
if st.button("Predict 🌼"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    input_scaled = scaler.transform(input_data)
    
    prediction = model.predict(input_scaled)[0]
    species = iris.target_names[prediction]

    st.success(f"Predicted Species: 🌸 {species}")
    
    # Evaluate Model
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    report_df = pd.DataFrame(
        classification_report(
            y_test,
            y_pred,
            target_names=iris.target_names,
            output_dict=True
        )
    ).transpose().round(2)

    # Display to user
    st.subheader("Model Performance")
    st.metric("Accuracy", f"{accuracy:.2%}")

    st.subheader("Classification Report")

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.dataframe(report_df)