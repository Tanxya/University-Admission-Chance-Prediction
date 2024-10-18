import streamlit as st
import pickle

def main():
    st.title("About This App")
    st.markdown("""
    ### University Admission Predictor
    This application uses machine learning to predict the chances of admission to a university based on several features such as GRE scores, TOEFL scores, and more.

    #### Features:
    - **GRE Score**: Graduate Record Examination score
    - **TOEFL Score**: Test of English as a Foreign Language score
    - **University Rating**: Rating of the university (1 to 5)
    - **SOP**: Statement of Purpose rating
    - **LOR**: Letter of Recommendation rating
    - **CGPA**: Cumulative Grade Point Average
    - **Research**: Whether the applicant has research experience (0 or 1)
    """)

    # Display feature importance
    st.markdown("### Feature Importance:")
    try:
        with open('admission_model.pkl', 'rb') as f:
            model = pickle.load(f)
        
        feature_importances = model.feature_importances_
        feature_names = ["GRE Score", "TOEFL Score", "University Rating", "SOP", "LOR", "CGPA", "Research"]
        
        for name, importance in zip(feature_names, feature_importances):
            st.write(f"**{name}:** {importance:.4f}")
    
    except Exception as e:
        st.error(f"Unable to load feature importance: {e}")

    st.markdown("""
    #### How It Works:
    The app uses a Random Forest Classifier model to predict whether you have a chance of admission based on your input data.
    """)

if __name__ == "__main__":
    main()
