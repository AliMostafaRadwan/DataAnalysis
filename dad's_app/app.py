import streamlit as st
import streamlit_authenticator as stauth
from main import main_page
from main import teacher_control


names = ['Ali Radwan','John Smith','Rebecca Briggs']
usernames = ['admin','jsmith','rbriggs']
passwords = ['admin','123','456']


hashed_passwords = stauth.Hasher(passwords).generate()





authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=1)


name, authentication_status, username = authenticator.login('Sign In','main')




if authentication_status and usernames[names.index(name)] != 'admin':
    main_page()
elif authentication_status == False:
    st.error('Username/password is incorrect')
if authentication_status and usernames[names.index(name)] == 'admin':
    teacher_control()




