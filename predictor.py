import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
import pickle
import streamlit as st

# Function to train the model (for initial setup, not needed in the Streamlit app)
def train_model(data):
    # Assuming the last column is the target variable
    X = data.iloc[:, :-1].values
    y = (data.iloc[:, -1].values >= 0.5).astype(int)  # Binarize the target variable

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train_scaled, y_train)

    # Check model accuracy
    train_accuracy = model.score(X_train_scaled, y_train)
    test_accuracy = model.score(X_test_scaled, y_test)
    print("Training accuracy:", train_accuracy)
    print("Test accuracy:", test_accuracy)

    # Save the scaler and model to file
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    with open('admission_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    return model, scaler

# Load the model and scaler
def load_model_and_scaler():
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('admission_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model, scaler

# Function to recommend universities based on prediction probability
def recommend_universities(probability):
    if probability > 80:
        return ["MIT", "Stanford", "Harvard"]
    elif 60 <= probability <= 80:
        return ["University of Michigan", "University of Texas"]
    else:
        return ["State University", "Regional College"]

# Streamlit app
def main():
    st.title("University Admission Predictor")

    st.markdown("### Please input your details below:")

    # Collect user input
    GRE_Score = st.number_input("GRE Score (Out of 340)", min_value=1, max_value=340, step=1)
    TOEFL_Score = st.number_input("TOEFL Score (Out of 120)", min_value=1, max_value=120, step=1)
    University_Rating = st.number_input("University Rating (1 - 5)", min_value=1, max_value=5, step=1)
    SOP = st.number_input("SOP (Out of 5.00)", min_value=0.0, max_value=5.0, step=0.1)
    LOR = st.number_input("LOR (Out of 5.00)", min_value=0.0, max_value=5.0, step=0.1)
    CGPA = st.number_input("CGPA (Out of 10.00)", min_value=1.0, max_value=10.0, step=0.1)
    Research = st.number_input("Research (0 or 1)", min_value=0, max_value=1, step=1)

    # Predict button
    if st.button("Predict"):
        try:
            # Load model and scaler
            model, scaler = load_model_and_scaler()

            features = [GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research]
            features_array = np.array(features).reshape(1, -1)

            # Scale the input features
            features_scaled = scaler.transform(features_array)

            # Make a prediction using the Random Forest model
            prediction_probability = model.predict_proba(features_scaled)[0][1] * 100  # Get probability of class 1
            prediction = model.predict(features_scaled)[0]

            # Recommend universities based on the predicted probability
            recommended_universities = recommend_universities(prediction_probability)

            # Center the image display
            col1, col2, col3 = st.columns([1, 3, 1])

            with col2:
                # Display result
                if prediction < 0.5:
                    st.image("nochance.png", caption="You don't have a chance.", width=250)
                else:
                    st.image("chance.jpg", caption="You have a chance.", width=250)
                
                st.write(f"Predicted Admission Probability: {prediction_probability:.2f}%")
                st.write("Based on your profile, you may have a chance of admission at the following universities:")
                for university in recommended_universities:
                    st.write(f"- {university}")
        except Exception as e:
            st.error(f"There was an error with your input: {e}")

if __name__ == "__main__":
    main()
