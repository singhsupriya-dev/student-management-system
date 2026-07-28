import streamlit as st
from student import Student

obj=Student()

st.title("Add Student")

with st.form("form"):
    name=st.text_input("Name")
    age=st.number_input("Age",1,100)
    branch=st.selectbox("Branch",["CSE","IT","ME","EE","EC","CE"])
    phone=st.text_input("Phone")
    email=st.text_input("Email")
    submit=st.form_submit_button("Save")

if submit:
     obj.add_student(name,age,branch,phone,email)
     st.success("Student Added Successfully")
