import streamlit as st

def main():
    st.title("University Rating")
    st.markdown("""
    ### University Rating

    **University Rating** is a numerical scale (1 to 5) indicating the reputation of the university.
    
    #### Importance:
    - Higher ratings often correspond to more competitive admissions processes.
    - Indicates the quality of education and resources available at the university.
    - Influences the perceived value of your degree.

    #### Rating Scale:
    - **1**: Low-rated university
    - **2**: Average-rated university
    - **3**: Good university
    - **4**: Very good university
    - **5**: Top-rated university

    #### Tips for Choosing a University:
    - **Research Thoroughly**: Understand the university's strengths, programs, and reputation.
    - **Consider Your Goals**: Choose a university that aligns with your academic and career goals.
    - **Look at Resources**: Evaluate the resources and facilities available to students.
    - **Check Alumni Network**: A strong alumni network can be beneficial for career opportunities.
    - **Visit Campuses**: If possible, visit campuses to get a feel for the environment and culture.
    """)

if __name__ == "__main__":
    main()
