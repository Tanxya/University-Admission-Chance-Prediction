# Predicting University Admission Chances

## Overview
This project is a system to predict university admission chances based on student profiles using classification algorithms. The project also features a user-friendly interface developed with Streamlit, enabling students to estimate their likelihood of admission interactively.

## Features
- Predicts the probability of admission to a university.
- Includes models like Logistic Regression, Random Forest, Decision Tree, and Support Vector Machine (SVM).
- Random Forest is the primary model used, as it outperformed other algorithms in accuracy.
- Displays feature importance to help understand which factors influence admission chances.
- Provides a simple and intuitive web application interface built with Streamlit.

## Dataset
The dataset includes:
- Standardized test scores (e.g., GRE, TOEFL)
- Academic performance (e.g., CGPA)
- University rating
- Research experience
- Personal statements
- Demographic information

## Installation
### Requirements
- Python 3.8+
- Streamlit
- Scikit-learn
- Pandas
- Numpy

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/university-admission-prediction.git
    ```
2. Navigate to the project directory:
    ```bash
    cd university-admission-prediction
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    streamlit run app.py
    ```

## Usage
1. Enter your academic and profile details in the web interface.
2. Click the "Predict" button to view your admission chances.
3. If the prediction is negative, a "Better luck next time" message will appear.

## Project Structure
- `app.py`: Main Streamlit application file.
- `models/`: Contains code for training and testing classification models.
- `data/`: Stores the dataset used for the project.
- `results/`: Includes evaluation metrics and visualizations.

## Models
- Logistic Regression
- Random Forest (primary model)
- Decision Tree
- Support Vector Machine

## Highlights
- Random Forest achieved the highest accuracy among all tested models.
- User-friendly UI built with Streamlit.

## Screenshots
1. **Feature Importance**
   ![Screenshot (542)](https://github.com/user-attachments/assets/0052a5f3-4189-4f72-80a2-836ac309a12f)

2. **App Interface**
   ![Screenshot 2024-08-16 193129](https://github.com/user-attachments/assets/68af1a97-5fc2-4d95-9103-790f6abcc47c)
   ![Screenshot 2024-08-16 193442](https://github.com/user-attachments/assets/c59135c0-4944-44c6-9d80-44eef31847d5)


## Future Work
- Enhance the dataset with more features.
- Integrate additional advanced algorithms.
- Deploy the application on a cloud platform.

---

- [Tanxya](https://github.com/Tanxya)  
- [Meghanasunkari](https://github.com/Meghanasunkari) — Co-developer

**Contributors**: Feel free to fork the repository and contribute!

If you encounter any issues or have suggestions, open an issue or reach out.
