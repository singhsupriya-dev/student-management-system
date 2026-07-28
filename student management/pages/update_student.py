import streamlit as st
from student import Student

obj = Student()

st.title("Update Student")

sid = st.number_input("Student ID", 1, step=1)

if st.button("Load"):
    st.session_state.student = obj.search_student(sid)

if "student" in st.session_state and st.session_state.student:
    s = st.session_state.student

    with st.form("update"):
        name = st.text_input("Name", s[1])
        age = st.number_input("Age", 1, 100, value=s[2])
        branch = st.text_input("Branch", s[3])
        phone = st.text_input("Phone", s[4])
        email = st.text_input("Email", s[5])

        submit = st.form_submit_button("Update")

    if submit:
        obj.update_student(sid, name, age, branch, phone, email)
        st.success("Student Successfully Updated")
