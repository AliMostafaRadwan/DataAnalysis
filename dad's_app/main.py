import streamlit as st

def teacher_control():
    st.title('Teacher Control Panel')
    
    global zoom 
    zoom = st.text_area('Enter your zoom link',key='zoom')
    global status
    status= st.radio('Class status',('Not started','In progress'))
    global assignements
    assignements = st.file_uploader('Upload your assignments for the students', type=['pdf'])
    global links
    links = st.text_area('Enter your links')
    with st.expander('Add more content'):
         st.file_uploader('upload more files', accept_multiple_files=True)
         st.text_area('Enter more links')
    return zoom,assignements,links,status
    



def teacher_announcements(zoom,assignements,links,status):
    
    st.subheader('Zoom link')
    with st.expander('Click to expand the link'):
        st.write(zoom)
    st.subheader('Assignments')
    with st.expander('Click to download the assignment/s'):
        st.subheader('assignments')

        if assignements is None:
            st.success('no assignments uploaded')
        else:
            st.download_button('HW.pdf',assignements)



    st.subheader('upload your assignment answers')
    st.file_uploader('Upload your assignment', type=['pdf'])

    st.subheader('Links you may need')
    with st.expander('Click to expand'):
        st.write(links)

    states = status
    st.subheader('Class states')
    if states == 'Not started':
        st.warning('Class is not started yet')
    elif states == 'In progress':
        st.success('Class is in progress')
    #return zoom,assignements,links,status



zoom,assignements,links,status = teacher_control()
def main_page():
    st.sidebar.title('Physics')
    gate = st.sidebar.selectbox('Rooms', ['Announcements', 'Syllabus'])
    
    if gate == 'Announcements':
       teacher_announcements(zoom,assignements,links,status)
        
    

#todo: show the 'more content'part to the student panel because it is now in the teacher panel
#todo: add a student system because it's not working with any accual students