import streamlit as st
from student import Student

obj = Student()

st.title("Delete Student")

sid = st.number_input("Student ID", 1, step=1)

if st.button("Delete"):
    obj.delete_student(sid)
    st.success("Student Deleted Successfully")