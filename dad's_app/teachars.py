import streamlit as st
from main import *




def teacher_control():
    st.title('Teacher Control Panel')
    
    global zoom 
    zoom = st.text_area('Enter your zoom link')
    global assignements
    assignements = st.file_uploader('Upload your assignments for the students', type=['pdf'])
    global links
    links = st.text_input('Enter your links')
    global status
    status= st.radio('Class status',('Not started','In progress'))
    return zoom,assignements,links,status

