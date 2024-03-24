import streamlit as st
import firebase_admin 
from firebase_admin import credentials, auth

 
cred = credentials.Certificate('ayurevedic-plant-detection-4911ef72fe25.json')
#firebase_admin.initialize_app(cred)

def app():
    st.title("Welcome to AyurVision")

    #choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    def f():
        try:
            user = auth.get_user_by_email(email)
            st.write('Login Successful')
            st.session_state.username = user.uid
            st.session_state.useremail = user.email

            st.session_state.signedout=True
            st.session_state.signout=True

        except:
            st.warning("Login Failed")
    def t():
        st.session_state.signedout=False
        st.session_state.signout=False
        st.session_state.useremail = ''

    if 'signedout' not in st.session_state:
        st.session_state.signedout=False

    if 'signout' not in st.session_state:
        st.session_state.signout=False   
    
    if not st.session_state['signedout']:
        choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])

        if choice == "Login":
            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')
        
            st.button('Login', on_click=f)

        else:
            username = st.text_input('User_Name')
            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')
        
            if st.button('Create my Account'):
                user = auth.create_user(email=email, password=password, uid=username)
                st.success('Account Created Successfully')
                st.markdown('Please login with your email and password')
                st.balloons()


    
    if st.session_state.signout:
        st.text('Name : '+st.session_state.username)
        st.text('Email id:'+st.session_state.useremail)
        st.button('Sign out',on_click=t)
