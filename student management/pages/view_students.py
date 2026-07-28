import streamlit as st
import pandas as pd
from student import Student

obj=Student()

st.title("View Students")

try:
    data=obj.view_students()
    if data:
        df=pd.DataFrame(data,columns=["ID","Name","Age","Branch","Phone","Email"])
        st.dataframe(df,use_container_width=True)
    else:
        st.info("No students found in the database.")
except Exception as e:
    st.error(f"Error fetching students: {str(e)}")