import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Grade Manager",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# Initialize session state
# --------------------------------------------------

if "students" not in st.session_state:
    st.session_state.students = []


# --------------------------------------------------
# Grading function
# --------------------------------------------------

def calculate_grade(mark):

    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🎓 Grade Manager")
st.write("Add students and their marks to calculate grades.")


# --------------------------------------------------
# Student form
# --------------------------------------------------

st.subheader("Add Student")

with st.form("student_form"):

    name = st.text_input("Student Name")

    mark = st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

    submitted = st.form_submit_button("Add Student")

    if submitted:

        if name.strip() == "":
            st.error("Please enter the student name.")

        else:
            grade = calculate_grade(mark)

            student = {
                "Name": name,
                "Mark": mark,
                "Grade": grade
            }

            st.session_state.students.append(student)

            st.success(f"{name} added successfully!")


# --------------------------------------------------
# Results table
# --------------------------------------------------

st.subheader("📋 Student Results")

if len(st.session_state.students) > 0:

    st.table(st.session_state.students)

else:

    st.info("No students have been added yet.")


# --------------------------------------------------
# Metrics
# --------------------------------------------------

if len(st.session_state.students) > 0:

    marks = [
        student["Mark"]
        for student in st.session_state.students
    ]

    class_average = sum(marks) / len(marks)
    highest_mark = max(marks)
    lowest_mark = min(marks)

    st.subheader("📊 Class Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Class Average",
            f"{class_average:.2f}"
        )

    with col2:
        st.metric(
            "Highest Mark",
            highest_mark
        )

    with col3:
        st.metric(
            "Lowest Mark",
            lowest_mark
        )