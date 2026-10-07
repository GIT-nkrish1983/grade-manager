import streamlit as st

students = []

name = st.text_input("Student Name")
mark = st.number_input("Mark")

if st.button("Add Student"):
    students.append({
        "Name": name,
        "Mark": mark
    })

st.table(students)