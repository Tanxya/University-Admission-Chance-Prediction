import streamlit as st
from streamlit import session_state as state
import subprocess
import sys

# Ensure session state is initialized
if 'predict' not in state:
    state.predict = False

# Function to load a page
def load_page(page):
    if page == "Home":
        st.write("Use the navigation menu above to explore different pages.")
    elif page == "This App":
        import pages.about as about
        about.main()
    elif page.startswith("Parameters - "):
        parameter = page.split(" - ")[1].lower()
        if parameter == "gre":
            import pages.parameters.gre as gre
            gre.main()
        elif parameter == "toefl":
            import pages.parameters.toefl as toefl
            toefl.main()
        elif parameter == "university rating":
            import pages.parameters.universityrating as universityrating
            universityrating.main()
        elif parameter == "sop":
            import pages.parameters.sop as sop
            sop.main()
        elif parameter == "lor":
            import pages.parameters.lor as lor
            lor.main()
        elif parameter == "cgpa":
            import pages.parameters.cgpa as cgpa
            cgpa.main()
        elif parameter == "research":
            import pages.parameters.research as research
            research.main()
    elif page == "Predictor":
        import pages.predictor as predictor
        predictor.main()

def main():
    st.title("Welcome to the University Admission Predictor!")

    # Main page navigation
    page = st.selectbox(
        "Know more about:",
        ["This App"] + [f"{p}" for p in ["GRE", "TOEFL", "University Rating", "SOP", "LOR", "CGPA", "Research"]] + ["Predictor"]
    )
    load_page(page)

    st.markdown("\n\nClick the button below to predict your chances of admission:")

    # When the "Let's Go" button is clicked, open a new command prompt and run predictor.py
    if st.button("Let's Go"):
        state.predict = True
        if sys.platform == "win32":  # For Windows
            subprocess.Popen(['start', 'cmd', '/k', 'streamlit run D:\\Sem-6\\LABS\\MiniProject\\project\\predictor.py'], shell=True)
        elif sys.platform == "darwin":  # For macOS
            subprocess.Popen(['open', '-a', 'Terminal', 'streamlit run D:\\Sem-6\\LABS\\MiniProject\\project\\predictor.py'])
        else:  # For Linux
            subprocess.Popen(['gnome-terminal', '--', 'streamlit run D:\\Sem-6\\LABS\\MiniProject\\project\\predictor.py'])
        st.rerun()  # To refresh the current page

if __name__ == "__main__":
    main()

