import streamlit as st
from student import Student

obj=Student()

st.title("Search Student")

sid=st.number_input("Student ID",1,step=1)

if st.button("Search"):
    data=obj.search_student(sid)
    if data:
        st.write({"ID":data[0],"Name":data[1],"Age":data[2],"Branch":data[3],"Phone":data[4],"Email":data[5]})
    else:
        st.error("Student Not Found")