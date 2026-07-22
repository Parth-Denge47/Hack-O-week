import streamlit as st
import pandas as pd
import numpy as np


# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="Student App",
    page_icon="🎓",
    layout="centered"
)


# -------------------------
# Custom CSS UI Design
# -------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

h1 {
    color: #1f4e79;
    text-align: center;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px gray;
    margin:10px;
}

.stButton button {
    background-color:#1f77b4;
    color:white;
    border-radius:10px;
    width:100%;
}

</style>

""", unsafe_allow_html=True)



# -------------------------
# Header
# -------------------------

st.title("🎓 Student Performance App")

st.write(
    "A basic UI application using Python, Pandas and NumPy"
)



# -------------------------
# Sidebar
# -------------------------

st.sidebar.header("Menu")

option = st.sidebar.selectbox(
    "Choose Option",
    [
        "Home",
        "Student Analysis"
    ]
)



# -------------------------
# Home Page
# -------------------------

if option == "Home":

    st.markdown("""
    <div class="card">

    <h3>Welcome 👋</h3>

    This application demonstrates:

    - Python Functions
    - NumPy Arrays
    - Pandas DataFrames
    - Simple UI Design

    </div>

    """,
    unsafe_allow_html=True)



# -------------------------
# Student Page
# -------------------------

else:


    st.subheader("Enter Student Details")


    name = st.text_input(
        "Student Name"
    )


    math = st.number_input(
        "Math Marks",
        0,
        100
    )


    science = st.number_input(
        "Science Marks",
        0,
        100
    )


    english = st.number_input(
        "English Marks",
        0,
        100
    )


    if st.button("Calculate Result"):


        # NumPy Array

        marks = np.array(
            [
                math,
                science,
                english
            ]
        )


        average = np.mean(marks)



        # Pandas DataFrame

        data = pd.DataFrame(
            {
                "Subject":
                [
                    "Math",
                    "Science",
                    "English"
                ],

                "Marks":
                marks
            }
        )


        st.success(
            f"{name}'s Average Mark: {average:.2f}"
        )


        st.markdown(
        """
        <div class="card">

        Result Summary

        </div>
        """,
        unsafe_allow_html=True
        )


        st.dataframe(
            data,
            use_container_width=True
        )



        # Chart

        st.bar_chart(
            data.set_index("Subject")
        )